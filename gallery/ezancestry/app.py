"""
## ezancestry

Visualize you genotypes using the One Thousand Genomes Project Populations.

Author: [Kevin ARvai](https://github.com/arvkevi))\n
Source: [Github](https://github.com/arvkevi/ezancestry)
"""
import warnings

import numpy as np
import pandas as pd
import streamlit as st

import plotly.express as px
import umap
from category_encoders.one_hot import OneHotEncoder
from cyvcf2 import VCF
from sklearn.decomposition import PCA
from sklearn.impute import KNNImputer
from sklearn.manifold import TSNE
from sklearn.neighbors import KNeighborsClassifier
from snps import SNPs

warnings.filterwarnings("ignore")
st.set_option('deprecation.showfileUploaderEncoding', False)


def main():
    # Render the readme as markdown using st.markdown.
    st.title("ezancestry")
    readme_text = st.markdown("""# Genetic Ancestry Visualization
The figure below displays samples from the [1000 Genomes Project](http://www.internationalgenome.org/home). What you are seeing are the samples' genotypes projected into a three-dimensional feature-space through dimensionality reduction techniques. Data points are colored according to a sample's [reported genetic ancestry](http://www.internationalgenome.org/faq/which-populations-are-part-your-study/).
The genotypes were filtered to include only a small subset of the genome called [ancestry-informative single nucleotide polymorphisms](https://en.wikipedia.org/wiki/Ancestry-informative_marker) (**AISNPs**). Then, the genotypes were one-hot encoded. Finally, dimensionality reduction was performed to facilitate visualization.
**You can also visualize your direct-to-consumer genetic results (e.g. [23andMe](https://customercare.23andme.com/hc/en-us/articles/212196868-Accessing-Your-Raw-Genetic-Data)). A k-nearest neighbors classifier will predict which of the populations you are most closely related to based on the AISNP genotypes.**""")

    # get the 1000 genomes samples
    dfsamples = get_1kg_samples()

    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("Visualization Settings")
    # select which set of SNPs to explore
    aisnp_set = st.sidebar.radio(
        "Set of ancestry-informative SNPs:",
        ("Kidd et al. 55 AISNPs", "Seldin et al. 128 AISNPs"),
    )
    if aisnp_set == "Kidd et al. 55 AISNPs":
        aisnps_1kg = vcf2df("data/Kidd.55AISNP.1kG.vcf", dfsamples)
    elif aisnp_set == "Seldin et al. 128 AISNPs":
        aisnps_1kg = vcf2df("data/Seldin.128AISNP.1kG.vcf", dfsamples)

    # Encode 1kg data
    X_encoded, encoder = encode_genotypes(aisnps_1kg)
    # Dimensionality reduction
    dimensionality_reduction_method = st.sidebar.radio(
        "Dimensionality reduction technique:", ("PCA", "UMAP", "t-SNE")
    )
    # perform dimensionality reduction on the 1kg set
    X_reduced, reducer = dimensionality_reduction(
        X_encoded, algorithm=dimensionality_reduction_method
    )

    # Which population to plot
    population_level = st.sidebar.radio(
        "Population Resolution:", ("super population", "population")
    )

    # predicted population
    knn = KNeighborsClassifier(n_neighbors=9, weights="distance", n_jobs=2)

    # upload the user genotypes file
    user_file = st.sidebar.file_uploader("Upload your genotypes:")
    # Collapsable user AISNPs DataFrame
    if user_file is not None:
        try:
            with st.spinner("Uploading your genotypes..."):
                userdf = SNPs(user_file.getvalue()).snps
        except Exception as e:
            st.error(
                f"Sorry, there was a problem processing your genotypes file.\n {e}"
            )
            user_file = None

        # filter and encode the user record
        user_record, aisnps_1kg = filter_user_genotypes(userdf, aisnps_1kg)
        user_encoded = encoder.transform(user_record)
        X_encoded = np.concatenate((X_encoded, user_encoded))
        del userdf

        # impute the user record and reduce the dimensions
        user_imputed = impute_missing(X_encoded)
        user_reduced = reducer.transform([user_imputed])
        # fit the knn before adding the user sample
        knn.fit(X_reduced, dfsamples[population_level])

        # concat the 1kg and user reduced arrays
        X_reduced = np.concatenate((X_reduced, user_reduced))
        dfsamples.loc["me"] = ["me"] * 3

        # plot
        plotly_3d = plot_3d(X_reduced, dfsamples, population_level)
        st.plotly_chart(plotly_3d, user_container_width=True)

        # predict the population for the user sample
        user_pop = knn.predict(user_reduced)[0]
        st.subheader(f"Your predicted {population_level}")
        st.text(f"Your predicted population using KNN classifier is {user_pop}")
        # show the predicted probabilities for each population
        st.subheader(f"Your predicted {population_level} probabilities")
        user_pop_probs = knn.predict_proba(user_reduced)
        user_probs_df = pd.DataFrame(
            [user_pop_probs[0]], columns=knn.classes_, index=["me"]
        )
        st.dataframe(user_probs_df)

        show_user_gts = st.sidebar.checkbox("Show Your Genotypes")
        if show_user_gts:
            user_table_title = "Genotypes of Ancestry-Informative SNPs in Your Sample"
            st.subheader(user_table_title)
            st.dataframe(user_record)

    else:
        # plot
        plotly_3d = plot_3d(X_reduced, dfsamples, population_level)
        st.plotly_chart(plotly_3d, user_container_width=True)

    # Collapsable 1000 Genomes sample table
    show_1kg = st.sidebar.checkbox("Show 1k Genomes Genotypes")
    if show_1kg is True:
        table_title = (
            "Genotypes of Ancestry-Informative SNPs in 1000 Genomes Project Samples"
        )
        with st.spinner("Loading 1k Genomes DataFrame"):
            st.subheader(table_title)
            st.dataframe(aisnps_1kg)

    # Render the readme as markdown using st.markdown.
    readme_text = st.markdown("""# Details

Depending on which company performed your genotyping, your sample might be missing information for some of the 55 (or 128) **AISNPs**. There is a basic implementation of scikit-learn's `KNNImputer` to impute missing genotypes in your sample based on your nearest neighbors in the feature-space.

* To show a table of your genotypes at the AISNP locations, check **Show Your Genotypes**.

* To show a table of the 1000 genomes samples genotypes at the AISNP locations, check **Show 1k Genomes Genotypes**.

## 1000 Genomes and AISNPs Data

A subset of 1000 Genomes Project samples' single nucleotide polymorphism(s), or, SNP(s) have been parsed from the [publicly available `.bcf` files](ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/supporting/bcf_files/).  
The subset of `SNPs` were chosen from two publications which identified **AISNPs**:
  * Set of 55 AISNPs. [Progress toward an efficient panel of SNPs for ancestry inference](https://www.ncbi.nlm.nih.gov/pubmed?db=pubmed&cmd=Retrieve&dopt=citation&list_uids=24508742). Kidd et al. 2014
  * Set of 128 AISNPs. [Ancestry informative marker sets for determining continental origin and admixture proportions in common populations in America.](https://www.ncbi.nlm.nih.gov/pubmed?cmd=Retrieve&dopt=citation&list_uids=18683858). Kosoy et al. 2009 (Seldin Lab)

## Parameters

**Set of AISNPs to use**  
* `Kidd 55 AISNPs`: Subset the 1kG data to the 55 SNPs listed in the manuscript.
* `Seldin 128 AISNPs`: Subset the 1kG data to the 128 SNPs listed in the manuscript.

**Dimensionality Reduction Algorithm**
* `PCA`: *Principal Component Analysis*
  * Fastest
  * [scikit-learn implementation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
* `T-SNE`: *t-Distributued Stochastic Neighbor Embedding*
  * Slow
  * [sckit-learn implementation](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) -- *not used*
  * [Multicore-TSNE implementation](https://github.com/DmitryUlyanov/Multicore-TSNE) -- *used here*
* `UMAP`: *Uniform Manifold Approximation and Projection*
  * Faster than t-SNE.
  * [umap-learn implementation](https://umap-learn.readthedocs.io/en/latest/)

**Population Resolution**
* `Super Population`: One of {AFR, AMR, EAS, EUR, SAS}.
* `Population`: One of the 26 populations listed [here](http://www.internationalgenome.org/faq/which-populations-are-part-your-study/).

## Code  
The code used to process this data is available on [GitHub](https://github.com/arvkevi/ezancestry).""")


def get_1kg_samples(onekg_samples="data/integrated_call_samples_v3.20130502.ALL.panel"):
    """Download the sample information for the 1000 Genomes Project

    :return: DataFrame of sample-level population information
    :rtype: pandas DataFrame
    """
    dfsamples = pd.read_csv(onekg_samples, sep="\t")
    dfsamples.set_index("sample", inplace=True)
    dfsamples.drop(columns=["Unnamed: 4", "Unnamed: 5"], inplace=True)
    dfsamples.columns = ["population", "super population", "gender"]
    return dfsamples


@st.cache(show_spinner=True)
def encode_genotypes(df):
    """One-hot encode the genotypes

    :param df: A DataFrame of samples with genotypes as columns
    :type df: pandas DataFrame
    :return: pandas DataFrame of one-hot encoded columns for genotypes and OHE instance
    :rtype: pandas DataFrame, OneHotEncoder instance
    """
    ohe = OneHotEncoder(cols=df.columns, handle_missing="return_nan")
    X = ohe.fit_transform(df)
    return pd.DataFrame(X, index=df.index), ohe


def dimensionality_reduction(X, algorithm="PCA"):
    """Reduce the dimensionality of the AISNPs
    :param X: One-hot encoded 1kG AISNPs.
    :type X: pandas DataFrame
    :param algorithm: The type of dimensionality reduction to perform.
        One of {PCA, UMAP, t-SNE}
    :type algorithm: str
    :returns: The transformed X DataFrame, reduced to 3 components by <algorithm>,
    and the dimensionality reduction Transformer object.
    """
    n_components = 3

    if algorithm == "PCA":
        reducer = PCA(n_components=n_components)
    elif algorithm == "t-SNE":
        reducer = TSNE(n_components=n_components, n_jobs=4)
    elif algorithm == "UMAP":
        reducer = umap.UMAP(
            n_components=n_components, min_dist=0.2, metric="dice", random_state=42
        )
    else:
        return None, None

    X_reduced = reducer.fit_transform(X.values)

    return pd.DataFrame(X_reduced, columns=["x", "y", "z"], index=X.index), reducer


@st.cache(show_spinner=True)
def filter_user_genotypes(userdf, aisnps_1kg):
    """Filter the user's uploaded genotypes to the AISNPs

    :param userdf: The user's DataFrame from SNPs
    :type userdf: pandas DataFrame
    :param aisnps_1kg: The DataFrame containing snps for the 1kg project samples
    :type aisnps_1kg: pandas DataFrame
    :return: The user's DataFrame of AISNPs as columns, The 1kg DataFrame with user appended
    :rtype: pandas DataFrame
    """
    user_record = pd.DataFrame(index=["your_sample"], columns=aisnps_1kg.columns)
    for snp in user_record.columns:
        try:
            user_record[snp] = userdf.loc[snp]["genotype"]
        except KeyError:
            continue
    aisnps_1kg = aisnps_1kg.append(user_record)
    return user_record, aisnps_1kg


@st.cache(show_spinner=True)
def impute_missing(aisnps_1kg):
    """Use scikit-learns KNNImputer to impute missing genotypes for AISNPs

    :param aisnps_1kg: DataFrame of all samples including user's encoded genotypes.
    :type aisnps_1kg: pandas DataFrame
    :return: DataFrame with nan values filled in my KNNImputer
    :rtype: pandas DataFrame
    """
    imputer = KNNImputer(n_neighbors=9)
    imputed_aisnps = imputer.fit_transform(aisnps_1kg)
    return np.rint(imputed_aisnps[-1])


@st.cache
def vcf2df(vcf_fname, dfsamples):
    """Convert a vcf file (from the 1kg AISNPs) to a pandas DataFrame

    :param vcf_fname: path to the vcf file with AISNPs for every 1kg sample
    :type vcf_fname: str
    :param dfsamples: DataFrame with sample-level info on each 1kg sample.
    :type dfsamples: pandas DataFrame
    :return: DataFrame with genotypes for AISNPs as columns and samples as rows.
    :rtype: pandas DataFrame
    """
    vcf_file = VCF(vcf_fname)
    df = pd.DataFrame(index=vcf_file.samples)
    for variant in vcf_file():
        df[variant.ID] = [gt.replace("|", "") for gt in variant.gt_bases]

    df = df.join(dfsamples, how="outer")

    return df


def plot_3d(X_reduced, dfsamples, pop):
    """Display the 3d scatter plot.

    :param X_reduced: DataFrame of all samples feature-space features.
    :type X_reduced: pandas DataFrame
    :param dfsamples: DataFrame witih sample-level info on each 1kg sample.
    :type dfsamples: pandas DataFrame
    :param pop: The population resolution to plot
    :type pop: str
    :return: plotly figure
    :rtype: plotly figure
    """
    X = np.hstack((X_reduced, dfsamples))
    columns = [
        "component_1",
        "component_2",
        "component_3",
        "population",
        "super population",
        "gender",
    ]
    df = pd.DataFrame(X, columns=columns, index=dfsamples.index)
    color_discrete_map = {"me": "rgb(0,0,0)"}
    df["size"] = 16
    if "me" in dfsamples.index.tolist():
        df["size"].loc["me"] = 75

    fig = px.scatter_3d(
        df,
        x="component_1",
        y="component_2",
        z="component_3",
        color=pop,
        color_discrete_map=color_discrete_map,
        symbol=pop,
        height=600,
        size="size",
        opacity=0.95,
        color_discrete_sequence=["#008fd5", "#fc4f30", "#e5ae38", "#6d904f", "#810f7c"],
    )
    if "me" not in dfsamples.index.tolist():
        fig.update_traces(marker=dict(size=2))

    return fig


if __name__ == "__main__":
    main()
