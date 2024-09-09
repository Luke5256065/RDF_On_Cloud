## RDF_on_Cloud

This repository contains the scripts, datasets, and results for an experimental project exploring RDF (Resource Description Framework) implementation in a cloud environment. The objective is to test the performance, scalability, and efficiency of processing RDF datasets in the cloud with single-machine system and multiple-machine system, under various conditions including loading on very large dataset and high-volume querying.

# Repository Structure

The repository is organized into the following main directories:

- datasets: Contains RDF datasets used in the experiment. These datasets vary in size and complexity to test scalability and performance under different conditions.

- result: Stores the results of all tests conducted during the experiment. This includes raw output data.

- scripts: Includes all the scripts used for data processing, loading RDF datasets into the cloud, querying, and conducting stress tests. 



# Overview of the Experiment
The project aims to evaluate the following aspects of RDF processing in the cloud:

1. Loading Efficiency: Measuring the time and resources required to load RDF datasets into the cloud environment.

2. Querying Performance: Testing the efficiency of RDF queries on datasets of varying sizes.

3. Stress Testing: Simulating high-volume querying using multiprocessing to represent real-world clients accessing the database simultaneously.

# How to Use This Repository

Prerequisites

- A cloud platform setup (GCP, AWS, Azure, etc.) with ubuntu 20.04
- Python 3.8+ with necessary libraries listed in `scripts/requirements.txt`


# Key Findings
System-wise:
1.  Several systems are outdated, with limited documentation and inactive communities, making it difficult to find resources for proper system setup.

2. During our experimentation with various instance configurations, we encountered issues with systems built from machine images, often requiring a complete system rebuild

Performance-wise: 
1. Massive computation resources needed for preparing the data, and additional storage space is needs while converting raw data into system compatible strucutre. 

# Future Work
Current open-source systems present limitations, leaving room for future research:

- Single-machine systems: While we focused on graph-based and relational databases, future work could explore systems like Hadoop, Spark, and cloud-based architectures.

- Multi-machine systems: We did not fully test open-source multi-machine systems; future research should include comprehensive evaluations of these platforms.

- Other systems: Neo4j, a non-RDF system, outperformed RDF-based systems in some cases, suggesting that future studies could investigate other systems that may offer better performance.



