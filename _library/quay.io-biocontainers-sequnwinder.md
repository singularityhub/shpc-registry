---
layout: container
name:  "quay.io/biocontainers/sequnwinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sequnwinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sequnwinder/container.yaml"
updated_at: "2024-01-23 02:46:41.748876"
latest: "0.1.4--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/sequnwinder"
aliases:
 - "dtc"
 - "enr"
 - "fasta-from-bed"
 - "fasta-re-match"
 - "index-fasta-file"
 - "meme-chip_html_to_tsv"
 - "momo"
 - "sequnwinder"
 - "streme"
 - "streme_xml_to_html"
 - "tgene"
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
 - "0.1.4--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for sequnwinder"
config: {"url": "https://biocontainers.pro/tools/sequnwinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sequnwinder", "latest": {"0.1.4--hdfd78af_1": "sha256:8cc85e27130f2aec854d4aafc10596a2159bf17bb28647c80d82faf89f7b1c5c"}, "tags": {"0.1.4--hdfd78af_1": "sha256:8cc85e27130f2aec854d4aafc10596a2159bf17bb28647c80d82faf89f7b1c5c"}, "docker": "quay.io/biocontainers/sequnwinder", "aliases": {"dtc": "/usr/local/bin/dtc", "enr": "/usr/local/bin/enr", "fasta-from-bed": "/usr/local/bin/fasta-from-bed", "fasta-re-match": "/usr/local/bin/fasta-re-match", "index-fasta-file": "/usr/local/bin/index-fasta-file", "meme-chip_html_to_tsv": "/usr/local/bin/meme-chip_html_to_tsv", "momo": "/usr/local/bin/momo", "sequnwinder": "/usr/local/bin/sequnwinder", "streme": "/usr/local/bin/streme", "streme_xml_to_html": "/usr/local/bin/streme_xml_to_html", "tgene": "/usr/local/bin/tgene", "alphtype": "/usr/local/bin/alphtype", "ama": "/usr/local/bin/ama", "ama-qvalues": "/usr/local/bin/ama-qvalues", "ame": "/usr/local/bin/ame", "beeml2meme": "/usr/local/bin/beeml2meme", "centrimo": "/usr/local/bin/centrimo", "ceqlogo": "/usr/local/bin/ceqlogo", "chen2meme": "/usr/local/bin/chen2meme", "clustalw2fasta": "/usr/local/bin/clustalw2fasta", "clustalw2phylip": "/usr/local/bin/clustalw2phylip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sequnwinder.
shpc-registry automated BioContainers addition for sequnwinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sequnwinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sequnwinder:0.1.4--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sequnwinder/0.1.4--hdfd78af_1
$ module help quay.io/biocontainers/sequnwinder/0.1.4--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sequnwinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sequnwinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sequnwinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sequnwinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sequnwinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sequnwinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dtc

```bash
$ singularity exec <container> /usr/local/bin/dtc
$ podman run --it --rm --entrypoint /usr/local/bin/dtc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dtc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enr

```bash
$ singularity exec <container> /usr/local/bin/enr
$ podman run --it --rm --entrypoint /usr/local/bin/enr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-from-bed

```bash
$ singularity exec <container> /usr/local/bin/fasta-from-bed
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-from-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-from-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-re-match

```bash
$ singularity exec <container> /usr/local/bin/fasta-re-match
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-re-match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-re-match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-fasta-file

```bash
$ singularity exec <container> /usr/local/bin/index-fasta-file
$ podman run --it --rm --entrypoint /usr/local/bin/index-fasta-file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-fasta-file   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### sequnwinder

```bash
$ singularity exec <container> /usr/local/bin/sequnwinder
$ podman run --it --rm --entrypoint /usr/local/bin/sequnwinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sequnwinder   -v ${PWD} -w ${PWD} <container> -c " $@"
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