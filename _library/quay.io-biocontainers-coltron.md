---
layout: container
name:  "quay.io/biocontainers/coltron"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/coltron/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/coltron/container.yaml"
updated_at: "2026-08-28 14:33:32.621160"
latest: "1.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/coltron"
aliases:
 - "add-security-constraint"
 - "bed2fasta"
 - "centrimo-plots"
 - "coltron"
 - "coltron-get-data"
 - "derangement"
 - "fasta-file-indexer"
 - "fasta-holdout-set"
 - "prosite2meme"
 - "sea"
 - "simplepp"
 - "tts"
 - "xstreme"
 - "xstreme_html_to_tsv"
 - "seq_cache_populate.py"
 - "streme"
 - "streme_xml_to_html"
 - "tgene"
 - "dtc"
 - "fasta-re-match"
 - "meme-chip_html_to_tsv"
 - "momo"
 - "alphtype"
 - "ama"
 - "ama-qvalues"
 - "ame"
 - "beeml2meme"
 - "centrimo"
 - "ceqlogo"
 - "chen2meme"
 - "clustalw2fasta"
 - "clustalw2phylip"
 - "compute-prior-dist"
 - "compute-uniform-priors"
 - "create-priors"
 - "dreme"
 - "dreme_xml_to_html"
 - "dreme_xml_to_txt"
 - "dust"
versions:
 - "1.0.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for coltron"
config: {"url": "https://biocontainers.pro/tools/coltron", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for coltron", "latest": {"1.0.2--pyhdfd78af_0": "sha256:82cb914415543b3ba31f6777d0710679698adb6cd410421733a64d1778abaf80"}, "tags": {"1.0.2--pyhdfd78af_0": "sha256:82cb914415543b3ba31f6777d0710679698adb6cd410421733a64d1778abaf80"}, "docker": "quay.io/biocontainers/coltron", "aliases": {"add-security-constraint": "/usr/local/bin/add-security-constraint", "bed2fasta": "/usr/local/bin/bed2fasta", "centrimo-plots": "/usr/local/bin/centrimo-plots", "coltron": "/usr/local/bin/coltron", "coltron-get-data": "/usr/local/bin/coltron-get-data", "derangement": "/usr/local/bin/derangement", "fasta-file-indexer": "/usr/local/bin/fasta-file-indexer", "fasta-holdout-set": "/usr/local/bin/fasta-holdout-set", "prosite2meme": "/usr/local/bin/prosite2meme", "sea": "/usr/local/bin/sea", "simplepp": "/usr/local/bin/simplepp", "tts": "/usr/local/bin/tts", "xstreme": "/usr/local/bin/xstreme", "xstreme_html_to_tsv": "/usr/local/bin/xstreme_html_to_tsv", "seq_cache_populate.py": "/usr/local/bin/seq_cache_populate.py", "streme": "/usr/local/bin/streme", "streme_xml_to_html": "/usr/local/bin/streme_xml_to_html", "tgene": "/usr/local/bin/tgene", "dtc": "/usr/local/bin/dtc", "fasta-re-match": "/usr/local/bin/fasta-re-match", "meme-chip_html_to_tsv": "/usr/local/bin/meme-chip_html_to_tsv", "momo": "/usr/local/bin/momo", "alphtype": "/usr/local/bin/alphtype", "ama": "/usr/local/bin/ama", "ama-qvalues": "/usr/local/bin/ama-qvalues", "ame": "/usr/local/bin/ame", "beeml2meme": "/usr/local/bin/beeml2meme", "centrimo": "/usr/local/bin/centrimo", "ceqlogo": "/usr/local/bin/ceqlogo", "chen2meme": "/usr/local/bin/chen2meme", "clustalw2fasta": "/usr/local/bin/clustalw2fasta", "clustalw2phylip": "/usr/local/bin/clustalw2phylip", "compute-prior-dist": "/usr/local/bin/compute-prior-dist", "compute-uniform-priors": "/usr/local/bin/compute-uniform-priors", "create-priors": "/usr/local/bin/create-priors", "dreme": "/usr/local/bin/dreme", "dreme_xml_to_html": "/usr/local/bin/dreme_xml_to_html", "dreme_xml_to_txt": "/usr/local/bin/dreme_xml_to_txt", "dust": "/usr/local/bin/dust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/coltron.
singularity registry hpc automated addition for coltron
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/coltron
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/coltron:1.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/coltron/1.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/coltron/1.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### coltron-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### coltron-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### coltron-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### coltron-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### coltron-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### coltron-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add-security-constraint

```bash
$ singularity exec <container> /usr/local/bin/add-security-constraint
$ podman run --it --rm --entrypoint /usr/local/bin/add-security-constraint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add-security-constraint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed2fasta

```bash
$ singularity exec <container> /usr/local/bin/bed2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/bed2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrimo-plots

```bash
$ singularity exec <container> /usr/local/bin/centrimo-plots
$ podman run --it --rm --entrypoint /usr/local/bin/centrimo-plots   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrimo-plots   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coltron

```bash
$ singularity exec <container> /usr/local/bin/coltron
$ podman run --it --rm --entrypoint /usr/local/bin/coltron   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coltron   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coltron-get-data

```bash
$ singularity exec <container> /usr/local/bin/coltron-get-data
$ podman run --it --rm --entrypoint /usr/local/bin/coltron-get-data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coltron-get-data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### derangement

```bash
$ singularity exec <container> /usr/local/bin/derangement
$ podman run --it --rm --entrypoint /usr/local/bin/derangement   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/derangement   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-file-indexer

```bash
$ singularity exec <container> /usr/local/bin/fasta-file-indexer
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-file-indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-file-indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-holdout-set

```bash
$ singularity exec <container> /usr/local/bin/fasta-holdout-set
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-holdout-set   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-holdout-set   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prosite2meme

```bash
$ singularity exec <container> /usr/local/bin/prosite2meme
$ podman run --it --rm --entrypoint /usr/local/bin/prosite2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prosite2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sea

```bash
$ singularity exec <container> /usr/local/bin/sea
$ podman run --it --rm --entrypoint /usr/local/bin/sea   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sea   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simplepp

```bash
$ singularity exec <container> /usr/local/bin/simplepp
$ podman run --it --rm --entrypoint /usr/local/bin/simplepp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simplepp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tts

```bash
$ singularity exec <container> /usr/local/bin/tts
$ podman run --it --rm --entrypoint /usr/local/bin/tts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xstreme

```bash
$ singularity exec <container> /usr/local/bin/xstreme
$ podman run --it --rm --entrypoint /usr/local/bin/xstreme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xstreme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xstreme_html_to_tsv

```bash
$ singularity exec <container> /usr/local/bin/xstreme_html_to_tsv
$ podman run --it --rm --entrypoint /usr/local/bin/xstreme_html_to_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xstreme_html_to_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_cache_populate.py

```bash
$ singularity exec <container> /usr/local/bin/seq_cache_populate.py
$ podman run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streme

```bash
$ singularity exec <container> /usr/local/bin/streme
$ podman run --it --rm --entrypoint /usr/local/bin/streme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streme_xml_to_html

```bash
$ singularity exec <container> /usr/local/bin/streme_xml_to_html
$ podman run --it --rm --entrypoint /usr/local/bin/streme_xml_to_html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streme_xml_to_html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tgene

```bash
$ singularity exec <container> /usr/local/bin/tgene
$ podman run --it --rm --entrypoint /usr/local/bin/tgene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tgene   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dtc

```bash
$ singularity exec <container> /usr/local/bin/dtc
$ podman run --it --rm --entrypoint /usr/local/bin/dtc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dtc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-re-match

```bash
$ singularity exec <container> /usr/local/bin/fasta-re-match
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-re-match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-re-match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meme-chip_html_to_tsv

```bash
$ singularity exec <container> /usr/local/bin/meme-chip_html_to_tsv
$ podman run --it --rm --entrypoint /usr/local/bin/meme-chip_html_to_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meme-chip_html_to_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### momo

```bash
$ singularity exec <container> /usr/local/bin/momo
$ podman run --it --rm --entrypoint /usr/local/bin/momo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/momo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alphtype

```bash
$ singularity exec <container> /usr/local/bin/alphtype
$ podman run --it --rm --entrypoint /usr/local/bin/alphtype   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alphtype   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ama

```bash
$ singularity exec <container> /usr/local/bin/ama
$ podman run --it --rm --entrypoint /usr/local/bin/ama   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ama   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ama-qvalues

```bash
$ singularity exec <container> /usr/local/bin/ama-qvalues
$ podman run --it --rm --entrypoint /usr/local/bin/ama-qvalues   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ama-qvalues   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ame

```bash
$ singularity exec <container> /usr/local/bin/ame
$ podman run --it --rm --entrypoint /usr/local/bin/ame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ame   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### beeml2meme

```bash
$ singularity exec <container> /usr/local/bin/beeml2meme
$ podman run --it --rm --entrypoint /usr/local/bin/beeml2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beeml2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrimo

```bash
$ singularity exec <container> /usr/local/bin/centrimo
$ podman run --it --rm --entrypoint /usr/local/bin/centrimo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrimo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ceqlogo

```bash
$ singularity exec <container> /usr/local/bin/ceqlogo
$ podman run --it --rm --entrypoint /usr/local/bin/ceqlogo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ceqlogo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chen2meme

```bash
$ singularity exec <container> /usr/local/bin/chen2meme
$ podman run --it --rm --entrypoint /usr/local/bin/chen2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chen2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalw2fasta

```bash
$ singularity exec <container> /usr/local/bin/clustalw2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/clustalw2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalw2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalw2phylip

```bash
$ singularity exec <container> /usr/local/bin/clustalw2phylip
$ podman run --it --rm --entrypoint /usr/local/bin/clustalw2phylip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalw2phylip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compute-prior-dist

```bash
$ singularity exec <container> /usr/local/bin/compute-prior-dist
$ podman run --it --rm --entrypoint /usr/local/bin/compute-prior-dist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute-prior-dist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compute-uniform-priors

```bash
$ singularity exec <container> /usr/local/bin/compute-uniform-priors
$ podman run --it --rm --entrypoint /usr/local/bin/compute-uniform-priors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute-uniform-priors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create-priors

```bash
$ singularity exec <container> /usr/local/bin/create-priors
$ podman run --it --rm --entrypoint /usr/local/bin/create-priors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create-priors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dreme

```bash
$ singularity exec <container> /usr/local/bin/dreme
$ podman run --it --rm --entrypoint /usr/local/bin/dreme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dreme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dreme_xml_to_html

```bash
$ singularity exec <container> /usr/local/bin/dreme_xml_to_html
$ podman run --it --rm --entrypoint /usr/local/bin/dreme_xml_to_html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dreme_xml_to_html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dreme_xml_to_txt

```bash
$ singularity exec <container> /usr/local/bin/dreme_xml_to_txt
$ podman run --it --rm --entrypoint /usr/local/bin/dreme_xml_to_txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dreme_xml_to_txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dust

```bash
$ singularity exec <container> /usr/local/bin/dust
$ podman run --it --rm --entrypoint /usr/local/bin/dust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dust   -v ${PWD} -w ${PWD} <container> -c " $@"
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