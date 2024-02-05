---
layout: container
name:  "quay.io/biocontainers/panacota"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/panacota/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/panacota/container.yaml"
updated_at: "2024-02-05 03:03:35.726813"
latest: "1.4.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/panacota"
aliases:
 - "PanACoTA"
 - "fastme"
 - "gimme_taxa.py"
 - "iqtree2"
 - "ncbi-genome-download"
 - "ngd"
 - "quicktree"
 - "run_panacota.py"
 - "tbl2asn-test"
 - "fix-sqn-date"
 - "faketime"
 - "real-tbl2asn"
 - "prokka-abricate_to_fasta_db"
 - "iqtree"
 - "prokka"
 - "prokka-biocyc_to_fasta_db"
 - "prokka-build_kingdom_dbs"
 - "prokka-cdd_to_hmm"
 - "prokka-clusters_to_hmm"
versions:
 - "1.3.1--pyhdfd78af_0"
 - "1.4.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for panacota"
config: {"url": "https://biocontainers.pro/tools/panacota", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for panacota", "latest": {"1.4.0--pyhdfd78af_0": "sha256:474fabc4d7715dfdc9e89206b87e34956369d360b05c8acee1e6ff050945f2a1"}, "tags": {"1.3.1--pyhdfd78af_0": "sha256:548c7236b039aac9e655b04cead23962566f77b2f2da1d21726334f4b457ad27", "1.4.0--pyhdfd78af_0": "sha256:474fabc4d7715dfdc9e89206b87e34956369d360b05c8acee1e6ff050945f2a1"}, "docker": "quay.io/biocontainers/panacota", "aliases": {"PanACoTA": "/usr/local/bin/PanACoTA", "fastme": "/usr/local/bin/fastme", "gimme_taxa.py": "/usr/local/bin/gimme_taxa.py", "iqtree2": "/usr/local/bin/iqtree2", "ncbi-genome-download": "/usr/local/bin/ncbi-genome-download", "ngd": "/usr/local/bin/ngd", "quicktree": "/usr/local/bin/quicktree", "run_panacota.py": "/usr/local/bin/run_panacota.py", "tbl2asn-test": "/usr/local/bin/tbl2asn-test", "fix-sqn-date": "/usr/local/bin/fix-sqn-date", "faketime": "/usr/local/bin/faketime", "real-tbl2asn": "/usr/local/bin/real-tbl2asn", "prokka-abricate_to_fasta_db": "/usr/local/bin/prokka-abricate_to_fasta_db", "iqtree": "/usr/local/bin/iqtree", "prokka": "/usr/local/bin/prokka", "prokka-biocyc_to_fasta_db": "/usr/local/bin/prokka-biocyc_to_fasta_db", "prokka-build_kingdom_dbs": "/usr/local/bin/prokka-build_kingdom_dbs", "prokka-cdd_to_hmm": "/usr/local/bin/prokka-cdd_to_hmm", "prokka-clusters_to_hmm": "/usr/local/bin/prokka-clusters_to_hmm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/panacota.
shpc-registry automated BioContainers addition for panacota
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/panacota
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/panacota:1.4.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/panacota/1.4.0--pyhdfd78af_0
$ module help quay.io/biocontainers/panacota/1.4.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### panacota-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### panacota-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### panacota-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### panacota-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### panacota-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### panacota-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PanACoTA

```bash
$ singularity exec <container> /usr/local/bin/PanACoTA
$ podman run --it --rm --entrypoint /usr/local/bin/PanACoTA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PanACoTA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastme

```bash
$ singularity exec <container> /usr/local/bin/fastme
$ podman run --it --rm --entrypoint /usr/local/bin/fastme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gimme_taxa.py

```bash
$ singularity exec <container> /usr/local/bin/gimme_taxa.py
$ podman run --it --rm --entrypoint /usr/local/bin/gimme_taxa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gimme_taxa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree2

```bash
$ singularity exec <container> /usr/local/bin/iqtree2
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi-genome-download

```bash
$ singularity exec <container> /usr/local/bin/ncbi-genome-download
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi-genome-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi-genome-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngd

```bash
$ singularity exec <container> /usr/local/bin/ngd
$ podman run --it --rm --entrypoint /usr/local/bin/ngd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quicktree

```bash
$ singularity exec <container> /usr/local/bin/quicktree
$ podman run --it --rm --entrypoint /usr/local/bin/quicktree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quicktree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_panacota.py

```bash
$ singularity exec <container> /usr/local/bin/run_panacota.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_panacota.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_panacota.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2asn-test

```bash
$ singularity exec <container> /usr/local/bin/tbl2asn-test
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix-sqn-date

```bash
$ singularity exec <container> /usr/local/bin/fix-sqn-date
$ podman run --it --rm --entrypoint /usr/local/bin/fix-sqn-date   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix-sqn-date   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faketime

```bash
$ singularity exec <container> /usr/local/bin/faketime
$ podman run --it --rm --entrypoint /usr/local/bin/faketime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faketime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### real-tbl2asn

```bash
$ singularity exec <container> /usr/local/bin/real-tbl2asn
$ podman run --it --rm --entrypoint /usr/local/bin/real-tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/real-tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-abricate_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-abricate_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-abricate_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-abricate_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree

```bash
$ singularity exec <container> /usr/local/bin/iqtree
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka

```bash
$ singularity exec <container> /usr/local/bin/prokka
$ podman run --it --rm --entrypoint /usr/local/bin/prokka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-biocyc_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-biocyc_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-biocyc_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-biocyc_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-build_kingdom_dbs

```bash
$ singularity exec <container> /usr/local/bin/prokka-build_kingdom_dbs
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-build_kingdom_dbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-build_kingdom_dbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-cdd_to_hmm

```bash
$ singularity exec <container> /usr/local/bin/prokka-cdd_to_hmm
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-cdd_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-cdd_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-clusters_to_hmm

```bash
$ singularity exec <container> /usr/local/bin/prokka-clusters_to_hmm
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-clusters_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-clusters_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
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