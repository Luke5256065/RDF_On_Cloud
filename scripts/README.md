## Script

This section provides essential scripts to help you quickly set up your environment and run benchmarks. The scripts are designed to streamline the installation process and execute the benchmarks with minimal configuration. Additionally, for distributed system setups, links to their latest repositories are provided.

# available setup scritps

- gstore_setup.sh
- neo4j_setup.sh
- virtuoso_setup.sh

usage: run sh {scrip_name} to install and build everyting in one go.

# Distributed System Setup

For setting up distributed systems, you can refer to the latest versions of their repositories. Below are the links to the recommended repositories for setting up a distributed environment:

PEG: https://gitee.com/ncuchenzeyu/peg

WUKONG: https://ipads.se.sjtu.edu.cn:1312/opensource/wukong

These repositories contain the most up-to-date instructions for installing, configuring, and deploying distributed systems. Follow the installation steps in the linked repositories to set up the distributed environment required for your benchmarks.


# Configuration

- Neo4j
    1. Download shell script and run the script to set up neo4j
    2. Go to `conf/neo4j.conf` to disable authentication
        
        a. Set dbms.default_database=`{dataset_name} `

        b. Uncomment the line dbms.security.auth_enabled=false 

        c. Add the line dbms.transaction.timeout=`30m`
    3. Run `bin/neo4j start` to start server
    4. Run `bin/cypher-shell` to run the console

To set up neo4j, you will need additional step, please run following commands in console:
    
    1. Constraint Creation
	CREATE CONSTRAINT n10s_unique_uri FOR (r:Resource) REQUIRE r.uri IS UNIQUE;
    2. call n10s.graphconfig.init();
    3. CALL n10s.graphconfig.set({ handleVocabUris: "IGNORE" });
With all above setsup and configure, you can now start to load and query on data on neo4j.

- Virtuoso

    1. go to virtuoso and make a copy of `virtuoso.ini.sample` configuration file
    2. add path of folder where you have you datasets to `DirsAllowed` Parameters
    3. Update `MaxQueryExecutionTime` to 1800 (for 30 minutes)

Save the configuration file and you are ready to go

# Load Data

- Neo4j
    1. Start neo4j start with `bin/neo4j start`
    2. Start neo4j console with `bin/cypher-shell`
    3. run following commands with url and dataformat params
`Call n10s.rdf.import.fetch("{file_url}", "{file_format}")`

- Virtuoso
    1. Start Virtuoso server with `bin/virtuoso-t -c wikidata.ini +foreground`
    2. Start Virtuoso console with `bin/isql localhost:1111`
    3. bulk load with command ld_dir('../data','*.nt', 'http://localhost:8890/{db_name}'); 
    4. run `rdf_loader_run();` to start loading

- Gstore 
    1. use `bin/ginit -db {db_name}` to initialize the database
    2. To create new db with data with `bin/gbuild -db {dbname} -f {filename}`
    3. to add more data with `bin/gadd -db {db_name} -f {filename}`

# Query

Please note that this repository does not include predefined query scripts for testing query performance. All queries were executed manually during the experiment. Queries can be found in the /datasets section. You can copy and paste these queries into the console to run the performance tests manually.

# Stress Testing

The stress testing script in this repository is a modified version of the script from the https://github.com/MillenniumDB/WDBench

We have provided two stress tests:

- One for Virtuoso
- One for GStore

To run the stress testing script, navigate to the appropriate system directory and execute:
`python3 script.py`



