---
layout: container
name:  "quay.io/biocontainers/cazy_webscraper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cazy_webscraper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cazy_webscraper/container.yaml"
updated_at: "2023-11-14 02:40:58.567293"
latest: "2.3.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cazy_webscraper"
aliases:
 - "cazy_webscraper"
 - "cw_extract_db_seqs"
 - "cw_get_genbank_seqs"
 - "cw_get_genomics"
 - "cw_get_gtdb_taxs"
 - "cw_get_ncbi_taxs"
 - "cw_get_pdb_structures"
 - "cw_get_uniprot_data"
 - "cw_query_database"
 - "xml2-config.bak"
 - "normalizer"
 - "tqdm"
 - "xslt-config"
 - "xsltproc"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
versions:
 - "2.2.1--pyhdfd78af_0"
 - "2.2.2--pyhdfd78af_0"
 - "2.2.7--pyhdfd78af_0"
 - "2.2.8--pyhdfd78af_0"
 - "2.3.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for cazy_webscraper"
config: {"url": "https://biocontainers.pro/tools/cazy_webscraper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cazy_webscraper", "latest": {"2.3.0--pyhdfd78af_0": "sha256:7588d753f99919d11d57a858e722ffbceeef435d6a284db6dd94d769b228adba"}, "tags": {"2.2.1--pyhdfd78af_0": "sha256:81c78834e559f3e523b48adcede93a4ba1c0e71e27cbbc9f7b8bcf8806c47b7b", "2.2.2--pyhdfd78af_0": "sha256:78070b07abdede9069e02e3bfeb88225c18911d9c8da208c00612c239c7a12eb", "2.2.7--pyhdfd78af_0": "sha256:c0cc4e274e22dd6cee2d11b62e049bd538ebe441fa750b10dfd61b4829962938", "2.2.8--pyhdfd78af_0": "sha256:9ae3fd1c302800b0776d4f6eb6918bea47c47b487b9a001fcce0cd8bd26b6e04", "2.3.0--pyhdfd78af_0": "sha256:7588d753f99919d11d57a858e722ffbceeef435d6a284db6dd94d769b228adba"}, "docker": "quay.io/biocontainers/cazy_webscraper", "aliases": {"cazy_webscraper": "/usr/local/bin/cazy_webscraper", "cw_extract_db_seqs": "/usr/local/bin/cw_extract_db_seqs", "cw_get_genbank_seqs": "/usr/local/bin/cw_get_genbank_seqs", "cw_get_genomics": "/usr/local/bin/cw_get_genomics", "cw_get_gtdb_taxs": "/usr/local/bin/cw_get_gtdb_taxs", "cw_get_ncbi_taxs": "/usr/local/bin/cw_get_ncbi_taxs", "cw_get_pdb_structures": "/usr/local/bin/cw_get_pdb_structures", "cw_get_uniprot_data": "/usr/local/bin/cw_get_uniprot_data", "cw_query_database": "/usr/local/bin/cw_query_database", "xml2-config.bak": "/usr/local/bin/xml2-config.bak", "normalizer": "/usr/local/bin/normalizer", "tqdm": "/usr/local/bin/tqdm", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cazy_webscraper.
shpc-registry automated BioContainers addition for cazy_webscraper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cazy_webscraper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cazy_webscraper:2.3.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cazy_webscraper/2.3.0--pyhdfd78af_0
$ module help quay.io/biocontainers/cazy_webscraper/2.3.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cazy_webscraper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cazy_webscraper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cazy_webscraper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cazy_webscraper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cazy_webscraper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cazy_webscraper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cazy_webscraper

```bash
$ singularity exec <container> /usr/local/bin/cazy_webscraper
$ podman run --it --rm --entrypoint /usr/local/bin/cazy_webscraper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cazy_webscraper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cw_extract_db_seqs

```bash
$ singularity exec <container> /usr/local/bin/cw_extract_db_seqs
$ podman run --it --rm --entrypoint /usr/local/bin/cw_extract_db_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cw_extract_db_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cw_get_genbank_seqs

```bash
$ singularity exec <container> /usr/local/bin/cw_get_genbank_seqs
$ podman run --it --rm --entrypoint /usr/local/bin/cw_get_genbank_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cw_get_genbank_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cw_get_genomics

```bash
$ singularity exec <container> /usr/local/bin/cw_get_genomics
$ podman run --it --rm --entrypoint /usr/local/bin/cw_get_genomics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cw_get_genomics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cw_get_gtdb_taxs

```bash
$ singularity exec <container> /usr/local/bin/cw_get_gtdb_taxs
$ podman run --it --rm --entrypoint /usr/local/bin/cw_get_gtdb_taxs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cw_get_gtdb_taxs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cw_get_ncbi_taxs

```bash
$ singularity exec <container> /usr/local/bin/cw_get_ncbi_taxs
$ podman run --it --rm --entrypoint /usr/local/bin/cw_get_ncbi_taxs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cw_get_ncbi_taxs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cw_get_pdb_structures

```bash
$ singularity exec <container> /usr/local/bin/cw_get_pdb_structures
$ podman run --it --rm --entrypoint /usr/local/bin/cw_get_pdb_structures   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cw_get_pdb_structures   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cw_get_uniprot_data

```bash
$ singularity exec <container> /usr/local/bin/cw_get_uniprot_data
$ podman run --it --rm --entrypoint /usr/local/bin/cw_get_uniprot_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cw_get_uniprot_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cw_query_database

```bash
$ singularity exec <container> /usr/local/bin/cw_query_database
$ podman run --it --rm --entrypoint /usr/local/bin/cw_query_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cw_query_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml2-config.bak

```bash
$ singularity exec <container> /usr/local/bin/xml2-config.bak
$ podman run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)