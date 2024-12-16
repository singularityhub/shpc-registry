---
layout: container
name:  "quay.io/biocontainers/pureclip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pureclip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pureclip/container.yaml"
updated_at: "2024-12-16 03:37:17.414218"
latest: "1.3.1--0"
container_url: "https://biocontainers.pro/tools/pureclip"
aliases:
 - "compute_CLmotif_scores.sh"
 - "dreme-py3"
 - "fasta-dinucleotide-shuffle-py3"
 - "fasta-hamming-enrich-py3"
 - "fasta-re-match"
 - "meme-chip_html_to_tsv"
 - "momo"
 - "pureclip"
 - "winextract"
 - "xsltproc_lite"
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
versions:
 - "1.3.1--0"
description: "shpc-registry automated BioContainers addition for pureclip"
config: {"url": "https://biocontainers.pro/tools/pureclip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pureclip", "latest": {"1.3.1--0": "sha256:6cb1ced18c68f3304d331bce888f6d1050e60eb325935953d10fcad533673b95"}, "tags": {"1.3.1--0": "sha256:6cb1ced18c68f3304d331bce888f6d1050e60eb325935953d10fcad533673b95"}, "docker": "quay.io/biocontainers/pureclip", "aliases": {"compute_CLmotif_scores.sh": "/usr/local/bin/compute_CLmotif_scores.sh", "dreme-py3": "/usr/local/bin/dreme-py3", "fasta-dinucleotide-shuffle-py3": "/usr/local/bin/fasta-dinucleotide-shuffle-py3", "fasta-hamming-enrich-py3": "/usr/local/bin/fasta-hamming-enrich-py3", "fasta-re-match": "/usr/local/bin/fasta-re-match", "meme-chip_html_to_tsv": "/usr/local/bin/meme-chip_html_to_tsv", "momo": "/usr/local/bin/momo", "pureclip": "/usr/local/bin/pureclip", "winextract": "/usr/local/bin/winextract", "xsltproc_lite": "/usr/local/bin/xsltproc_lite", "alphtype": "/usr/local/bin/alphtype", "ama": "/usr/local/bin/ama", "ama-qvalues": "/usr/local/bin/ama-qvalues", "ame": "/usr/local/bin/ame", "beeml2meme": "/usr/local/bin/beeml2meme", "centrimo": "/usr/local/bin/centrimo", "ceqlogo": "/usr/local/bin/ceqlogo", "chen2meme": "/usr/local/bin/chen2meme", "clustalw2fasta": "/usr/local/bin/clustalw2fasta", "clustalw2phylip": "/usr/local/bin/clustalw2phylip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pureclip.
shpc-registry automated BioContainers addition for pureclip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pureclip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pureclip:1.3.1--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pureclip/1.3.1--0
$ module help quay.io/biocontainers/pureclip/1.3.1--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pureclip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pureclip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pureclip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pureclip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pureclip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pureclip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compute_CLmotif_scores.sh

```bash
$ singularity exec <container> /usr/local/bin/compute_CLmotif_scores.sh
$ podman run --it --rm --entrypoint /usr/local/bin/compute_CLmotif_scores.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute_CLmotif_scores.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dreme-py3

```bash
$ singularity exec <container> /usr/local/bin/dreme-py3
$ podman run --it --rm --entrypoint /usr/local/bin/dreme-py3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dreme-py3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-dinucleotide-shuffle-py3

```bash
$ singularity exec <container> /usr/local/bin/fasta-dinucleotide-shuffle-py3
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-dinucleotide-shuffle-py3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-dinucleotide-shuffle-py3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-hamming-enrich-py3

```bash
$ singularity exec <container> /usr/local/bin/fasta-hamming-enrich-py3
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-hamming-enrich-py3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-hamming-enrich-py3   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pureclip

```bash
$ singularity exec <container> /usr/local/bin/pureclip
$ podman run --it --rm --entrypoint /usr/local/bin/pureclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pureclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### winextract

```bash
$ singularity exec <container> /usr/local/bin/winextract
$ podman run --it --rm --entrypoint /usr/local/bin/winextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/winextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc_lite

```bash
$ singularity exec <container> /usr/local/bin/xsltproc_lite
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc_lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc_lite   -v ${PWD} -w ${PWD} <container> -c " $@"
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