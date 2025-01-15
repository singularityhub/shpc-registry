---
layout: container
name:  "quay.io/biocontainers/cured"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cured/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cured/container.yaml"
updated_at: "2025-01-15 03:14:20.656328"
latest: "1.05--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/cured"
aliases:
 - "Bifrost"
 - "CURED_FindREs.py"
 - "CURED_Main.py"
 - "dataformat"
 - "datasets"
 - "mlst"
 - "mlst-ST_mini_genomes"
 - "mlst-consistency_checker"
 - "mlst-download_pub_mlst"
 - "mlst-make_blast_db"
 - "mlst-show_seqs"
 - "unitig-caller"
 - "TMalign"
 - "archive-ncbinlp"
 - "archive-nihocc"
 - "archive-nmcds"
 - "archive-pmc"
 - "archive-taxonomy"
 - "args2slice"
 - "asn2ref"
 - "blst2gm"
 - "cit2pmid"
 - "combine-uid-lists"
 - "difference-uid-lists"
 - "download-pmc"
 - "ds2pme"
 - "fetch-local"
 - "fetch-nmcds"
 - "fetch-pmc"
 - "fetch-taxonomy"
 - "filter-genbank"
 - "filter-record"
 - "gawk-5.3.0"
 - "gbf2fsa"
 - "gbf2ref"
 - "gm2ranges"
 - "gm2segs"
versions:
 - "1.05--hdfd78af_0"
description: "singularity registry hpc automated addition for cured"
config: {"url": "https://biocontainers.pro/tools/cured", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cured", "latest": {"1.05--hdfd78af_0": "sha256:785ade3df94f43bf3aad1f6c972152c01e45725e8a6f6cd5a9b7ccf02bcfd4b8"}, "tags": {"1.05--hdfd78af_0": "sha256:785ade3df94f43bf3aad1f6c972152c01e45725e8a6f6cd5a9b7ccf02bcfd4b8"}, "docker": "quay.io/biocontainers/cured", "aliases": {"Bifrost": "/usr/local/bin/Bifrost", "CURED_FindREs.py": "/usr/local/bin/CURED_FindREs.py", "CURED_Main.py": "/usr/local/bin/CURED_Main.py", "dataformat": "/usr/local/bin/dataformat", "datasets": "/usr/local/bin/datasets", "mlst": "/usr/local/bin/mlst", "mlst-ST_mini_genomes": "/usr/local/bin/mlst-ST_mini_genomes", "mlst-consistency_checker": "/usr/local/bin/mlst-consistency_checker", "mlst-download_pub_mlst": "/usr/local/bin/mlst-download_pub_mlst", "mlst-make_blast_db": "/usr/local/bin/mlst-make_blast_db", "mlst-show_seqs": "/usr/local/bin/mlst-show_seqs", "unitig-caller": "/usr/local/bin/unitig-caller", "TMalign": "/usr/local/bin/TMalign", "archive-ncbinlp": "/usr/local/bin/archive-ncbinlp", "archive-nihocc": "/usr/local/bin/archive-nihocc", "archive-nmcds": "/usr/local/bin/archive-nmcds", "archive-pmc": "/usr/local/bin/archive-pmc", "archive-taxonomy": "/usr/local/bin/archive-taxonomy", "args2slice": "/usr/local/bin/args2slice", "asn2ref": "/usr/local/bin/asn2ref", "blst2gm": "/usr/local/bin/blst2gm", "cit2pmid": "/usr/local/bin/cit2pmid", "combine-uid-lists": "/usr/local/bin/combine-uid-lists", "difference-uid-lists": "/usr/local/bin/difference-uid-lists", "download-pmc": "/usr/local/bin/download-pmc", "ds2pme": "/usr/local/bin/ds2pme", "fetch-local": "/usr/local/bin/fetch-local", "fetch-nmcds": "/usr/local/bin/fetch-nmcds", "fetch-pmc": "/usr/local/bin/fetch-pmc", "fetch-taxonomy": "/usr/local/bin/fetch-taxonomy", "filter-genbank": "/usr/local/bin/filter-genbank", "filter-record": "/usr/local/bin/filter-record", "gawk-5.3.0": "/usr/local/bin/gawk-5.3.0", "gbf2fsa": "/usr/local/bin/gbf2fsa", "gbf2ref": "/usr/local/bin/gbf2ref", "gm2ranges": "/usr/local/bin/gm2ranges", "gm2segs": "/usr/local/bin/gm2segs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cured.
singularity registry hpc automated addition for cured
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cured
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cured:1.05--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cured/1.05--hdfd78af_0
$ module help quay.io/biocontainers/cured/1.05--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cured-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cured-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cured-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cured-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cured-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cured-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Bifrost

```bash
$ singularity exec <container> /usr/local/bin/Bifrost
$ podman run --it --rm --entrypoint /usr/local/bin/Bifrost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Bifrost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CURED_FindREs.py

```bash
$ singularity exec <container> /usr/local/bin/CURED_FindREs.py
$ podman run --it --rm --entrypoint /usr/local/bin/CURED_FindREs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CURED_FindREs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CURED_Main.py

```bash
$ singularity exec <container> /usr/local/bin/CURED_Main.py
$ podman run --it --rm --entrypoint /usr/local/bin/CURED_Main.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CURED_Main.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dataformat

```bash
$ singularity exec <container> /usr/local/bin/dataformat
$ podman run --it --rm --entrypoint /usr/local/bin/dataformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dataformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datasets

```bash
$ singularity exec <container> /usr/local/bin/datasets
$ podman run --it --rm --entrypoint /usr/local/bin/datasets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datasets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst

```bash
$ singularity exec <container> /usr/local/bin/mlst
$ podman run --it --rm --entrypoint /usr/local/bin/mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst-ST_mini_genomes

```bash
$ singularity exec <container> /usr/local/bin/mlst-ST_mini_genomes
$ podman run --it --rm --entrypoint /usr/local/bin/mlst-ST_mini_genomes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst-ST_mini_genomes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst-consistency_checker

```bash
$ singularity exec <container> /usr/local/bin/mlst-consistency_checker
$ podman run --it --rm --entrypoint /usr/local/bin/mlst-consistency_checker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst-consistency_checker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst-download_pub_mlst

```bash
$ singularity exec <container> /usr/local/bin/mlst-download_pub_mlst
$ podman run --it --rm --entrypoint /usr/local/bin/mlst-download_pub_mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst-download_pub_mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst-make_blast_db

```bash
$ singularity exec <container> /usr/local/bin/mlst-make_blast_db
$ podman run --it --rm --entrypoint /usr/local/bin/mlst-make_blast_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst-make_blast_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst-show_seqs

```bash
$ singularity exec <container> /usr/local/bin/mlst-show_seqs
$ podman run --it --rm --entrypoint /usr/local/bin/mlst-show_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst-show_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unitig-caller

```bash
$ singularity exec <container> /usr/local/bin/unitig-caller
$ podman run --it --rm --entrypoint /usr/local/bin/unitig-caller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unitig-caller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TMalign

```bash
$ singularity exec <container> /usr/local/bin/TMalign
$ podman run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-ncbinlp

```bash
$ singularity exec <container> /usr/local/bin/archive-ncbinlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-ncbinlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-ncbinlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nihocc

```bash
$ singularity exec <container> /usr/local/bin/archive-nihocc
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nihocc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nihocc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nmcds

```bash
$ singularity exec <container> /usr/local/bin/archive-nmcds
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nmcds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nmcds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pmc

```bash
$ singularity exec <container> /usr/local/bin/archive-pmc
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-taxonomy

```bash
$ singularity exec <container> /usr/local/bin/archive-taxonomy
$ podman run --it --rm --entrypoint /usr/local/bin/archive-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### args2slice

```bash
$ singularity exec <container> /usr/local/bin/args2slice
$ podman run --it --rm --entrypoint /usr/local/bin/args2slice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/args2slice   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn2ref

```bash
$ singularity exec <container> /usr/local/bin/asn2ref
$ podman run --it --rm --entrypoint /usr/local/bin/asn2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blst2gm

```bash
$ singularity exec <container> /usr/local/bin/blst2gm
$ podman run --it --rm --entrypoint /usr/local/bin/blst2gm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blst2gm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cit2pmid

```bash
$ singularity exec <container> /usr/local/bin/cit2pmid
$ podman run --it --rm --entrypoint /usr/local/bin/cit2pmid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cit2pmid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine-uid-lists

```bash
$ singularity exec <container> /usr/local/bin/combine-uid-lists
$ podman run --it --rm --entrypoint /usr/local/bin/combine-uid-lists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine-uid-lists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### difference-uid-lists

```bash
$ singularity exec <container> /usr/local/bin/difference-uid-lists
$ podman run --it --rm --entrypoint /usr/local/bin/difference-uid-lists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/difference-uid-lists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-pmc

```bash
$ singularity exec <container> /usr/local/bin/download-pmc
$ podman run --it --rm --entrypoint /usr/local/bin/download-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ds2pme

```bash
$ singularity exec <container> /usr/local/bin/ds2pme
$ podman run --it --rm --entrypoint /usr/local/bin/ds2pme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ds2pme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-local

```bash
$ singularity exec <container> /usr/local/bin/fetch-local
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-local   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-local   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-nmcds

```bash
$ singularity exec <container> /usr/local/bin/fetch-nmcds
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-nmcds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-nmcds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-pmc

```bash
$ singularity exec <container> /usr/local/bin/fetch-pmc
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-taxonomy

```bash
$ singularity exec <container> /usr/local/bin/fetch-taxonomy
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-genbank

```bash
$ singularity exec <container> /usr/local/bin/filter-genbank
$ podman run --it --rm --entrypoint /usr/local/bin/filter-genbank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-genbank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-record

```bash
$ singularity exec <container> /usr/local/bin/filter-record
$ podman run --it --rm --entrypoint /usr/local/bin/filter-record   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-record   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2fsa

```bash
$ singularity exec <container> /usr/local/bin/gbf2fsa
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2fsa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2fsa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2ref

```bash
$ singularity exec <container> /usr/local/bin/gbf2ref
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gm2ranges

```bash
$ singularity exec <container> /usr/local/bin/gm2ranges
$ podman run --it --rm --entrypoint /usr/local/bin/gm2ranges   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gm2ranges   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gm2segs

```bash
$ singularity exec <container> /usr/local/bin/gm2segs
$ podman run --it --rm --entrypoint /usr/local/bin/gm2segs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gm2segs   -v ${PWD} -w ${PWD} <container> -c " $@"
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