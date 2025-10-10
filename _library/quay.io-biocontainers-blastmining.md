---
layout: container
name:  "quay.io/biocontainers/blastmining"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blastmining/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/blastmining/container.yaml"
updated_at: "2025-10-10 03:10:18.720320"
latest: "1.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/blastmining"
aliases:
 - "blastMining"
 - "blastMining_lca.sh"
 - "blastMining_lca2.sh"
 - "csvtk"
 - "f2py3.11"
 - "ktClassifyHits"
 - "ktImportHits"
 - "run_besthit.py"
 - "run_lca.py"
 - "run_vote.py"
 - "run_voteSpecies.py"
 - "tab2krona.py"
 - "taxonkit"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "ktClassifyBLAST"
 - "ktGetContigMagnitudes"
 - "ktGetLCA"
 - "ktGetLibPath"
 - "ktGetTaxIDFromAcc"
 - "ktGetTaxInfo"
 - "ktImportBLAST"
 - "ktImportDiskUsage"
 - "ktImportEC"
 - "ktImportFCP"
 - "ktImportGalaxy"
 - "ktImportKrona"
 - "ktImportMETAREP-BLAST"
 - "ktImportMETAREP-EC"
 - "ktImportMGRAST"
 - "ktImportPhymmBL"
 - "ktImportRDP"
 - "ktImportRDPComparison"
 - "ktImportTaxonomy"
 - "ktImportText"
versions:
 - "1.2.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for blastmining"
config: {"url": "https://biocontainers.pro/tools/blastmining", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for blastmining", "latest": {"1.2.0--pyhdfd78af_0": "sha256:3a4d520225a1892279b8805df885cb1003813e3e9e32593f77a3063db51ed71f"}, "tags": {"1.2.0--pyhdfd78af_0": "sha256:3a4d520225a1892279b8805df885cb1003813e3e9e32593f77a3063db51ed71f"}, "docker": "quay.io/biocontainers/blastmining", "aliases": {"blastMining": "/usr/local/bin/blastMining", "blastMining_lca.sh": "/usr/local/bin/blastMining_lca.sh", "blastMining_lca2.sh": "/usr/local/bin/blastMining_lca2.sh", "csvtk": "/usr/local/bin/csvtk", "f2py3.11": "/usr/local/bin/f2py3.11", "ktClassifyHits": "/usr/local/bin/ktClassifyHits", "ktImportHits": "/usr/local/bin/ktImportHits", "run_besthit.py": "/usr/local/bin/run_besthit.py", "run_lca.py": "/usr/local/bin/run_lca.py", "run_vote.py": "/usr/local/bin/run_vote.py", "run_voteSpecies.py": "/usr/local/bin/run_voteSpecies.py", "tab2krona.py": "/usr/local/bin/tab2krona.py", "taxonkit": "/usr/local/bin/taxonkit", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "ktClassifyBLAST": "/usr/local/bin/ktClassifyBLAST", "ktGetContigMagnitudes": "/usr/local/bin/ktGetContigMagnitudes", "ktGetLCA": "/usr/local/bin/ktGetLCA", "ktGetLibPath": "/usr/local/bin/ktGetLibPath", "ktGetTaxIDFromAcc": "/usr/local/bin/ktGetTaxIDFromAcc", "ktGetTaxInfo": "/usr/local/bin/ktGetTaxInfo", "ktImportBLAST": "/usr/local/bin/ktImportBLAST", "ktImportDiskUsage": "/usr/local/bin/ktImportDiskUsage", "ktImportEC": "/usr/local/bin/ktImportEC", "ktImportFCP": "/usr/local/bin/ktImportFCP", "ktImportGalaxy": "/usr/local/bin/ktImportGalaxy", "ktImportKrona": "/usr/local/bin/ktImportKrona", "ktImportMETAREP-BLAST": "/usr/local/bin/ktImportMETAREP-BLAST", "ktImportMETAREP-EC": "/usr/local/bin/ktImportMETAREP-EC", "ktImportMGRAST": "/usr/local/bin/ktImportMGRAST", "ktImportPhymmBL": "/usr/local/bin/ktImportPhymmBL", "ktImportRDP": "/usr/local/bin/ktImportRDP", "ktImportRDPComparison": "/usr/local/bin/ktImportRDPComparison", "ktImportTaxonomy": "/usr/local/bin/ktImportTaxonomy", "ktImportText": "/usr/local/bin/ktImportText"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/blastmining.
singularity registry hpc automated addition for blastmining
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blastmining
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blastmining:1.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blastmining/1.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/blastmining/1.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blastmining-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blastmining-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blastmining-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blastmining-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blastmining-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blastmining-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### blastMining

```bash
$ singularity exec <container> /usr/local/bin/blastMining
$ podman run --it --rm --entrypoint /usr/local/bin/blastMining   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastMining   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastMining_lca.sh

```bash
$ singularity exec <container> /usr/local/bin/blastMining_lca.sh
$ podman run --it --rm --entrypoint /usr/local/bin/blastMining_lca.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastMining_lca.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastMining_lca2.sh

```bash
$ singularity exec <container> /usr/local/bin/blastMining_lca2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/blastMining_lca2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastMining_lca2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csvtk

```bash
$ singularity exec <container> /usr/local/bin/csvtk
$ podman run --it --rm --entrypoint /usr/local/bin/csvtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvtk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktClassifyHits

```bash
$ singularity exec <container> /usr/local/bin/ktClassifyHits
$ podman run --it --rm --entrypoint /usr/local/bin/ktClassifyHits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktClassifyHits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportHits

```bash
$ singularity exec <container> /usr/local/bin/ktImportHits
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportHits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportHits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_besthit.py

```bash
$ singularity exec <container> /usr/local/bin/run_besthit.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_besthit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_besthit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_lca.py

```bash
$ singularity exec <container> /usr/local/bin/run_lca.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_lca.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_lca.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_vote.py

```bash
$ singularity exec <container> /usr/local/bin/run_vote.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_vote.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_vote.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_voteSpecies.py

```bash
$ singularity exec <container> /usr/local/bin/run_voteSpecies.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_voteSpecies.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_voteSpecies.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tab2krona.py

```bash
$ singularity exec <container> /usr/local/bin/tab2krona.py
$ podman run --it --rm --entrypoint /usr/local/bin/tab2krona.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tab2krona.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonkit

```bash
$ singularity exec <container> /usr/local/bin/taxonkit
$ podman run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktClassifyBLAST

```bash
$ singularity exec <container> /usr/local/bin/ktClassifyBLAST
$ podman run --it --rm --entrypoint /usr/local/bin/ktClassifyBLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktClassifyBLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetContigMagnitudes

```bash
$ singularity exec <container> /usr/local/bin/ktGetContigMagnitudes
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetContigMagnitudes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetContigMagnitudes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetLCA

```bash
$ singularity exec <container> /usr/local/bin/ktGetLCA
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetLCA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetLCA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetLibPath

```bash
$ singularity exec <container> /usr/local/bin/ktGetLibPath
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetLibPath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetLibPath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetTaxIDFromAcc

```bash
$ singularity exec <container> /usr/local/bin/ktGetTaxIDFromAcc
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetTaxIDFromAcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetTaxIDFromAcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetTaxInfo

```bash
$ singularity exec <container> /usr/local/bin/ktGetTaxInfo
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetTaxInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetTaxInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportBLAST

```bash
$ singularity exec <container> /usr/local/bin/ktImportBLAST
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportBLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportBLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportDiskUsage

```bash
$ singularity exec <container> /usr/local/bin/ktImportDiskUsage
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportDiskUsage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportDiskUsage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportEC

```bash
$ singularity exec <container> /usr/local/bin/ktImportEC
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportEC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportEC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportFCP

```bash
$ singularity exec <container> /usr/local/bin/ktImportFCP
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportFCP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportFCP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportGalaxy

```bash
$ singularity exec <container> /usr/local/bin/ktImportGalaxy
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportGalaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportGalaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportKrona

```bash
$ singularity exec <container> /usr/local/bin/ktImportKrona
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportKrona   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportKrona   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportMETAREP-BLAST

```bash
$ singularity exec <container> /usr/local/bin/ktImportMETAREP-BLAST
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportMETAREP-BLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportMETAREP-BLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportMETAREP-EC

```bash
$ singularity exec <container> /usr/local/bin/ktImportMETAREP-EC
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportMETAREP-EC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportMETAREP-EC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportMGRAST

```bash
$ singularity exec <container> /usr/local/bin/ktImportMGRAST
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportMGRAST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportMGRAST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportPhymmBL

```bash
$ singularity exec <container> /usr/local/bin/ktImportPhymmBL
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportPhymmBL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportPhymmBL   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportRDP

```bash
$ singularity exec <container> /usr/local/bin/ktImportRDP
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportRDP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportRDP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportRDPComparison

```bash
$ singularity exec <container> /usr/local/bin/ktImportRDPComparison
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportRDPComparison   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportRDPComparison   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportTaxonomy

```bash
$ singularity exec <container> /usr/local/bin/ktImportTaxonomy
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportTaxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportTaxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportText

```bash
$ singularity exec <container> /usr/local/bin/ktImportText
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportText   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportText   -v ${PWD} -w ${PWD} <container> -c " $@"
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