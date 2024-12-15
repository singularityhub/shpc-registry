---
layout: container
name:  "quay.io/biocontainers/chexmix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chexmix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chexmix/container.yaml"
updated_at: "2024-12-15 04:17:50.203485"
latest: "0.52--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/chexmix"
aliases:
 - "centrimo-plots"
 - "chexmix"
 - "dtc"
 - "fasta-from-bed"
 - "fasta-holdout-set"
 - "fasta-re-match"
 - "index-fasta-file"
 - "meme-chip_html_to_tsv"
 - "momo"
 - "sea"
 - "streme"
 - "streme_xml_to_html"
 - "tgene"
 - "xstreme"
 - "xstreme_html_to_tsv"
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
 - "0.52--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for chexmix"
config: {"url": "https://biocontainers.pro/tools/chexmix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chexmix", "latest": {"0.52--hdfd78af_0": "sha256:ffd9cf92a820c25ccc05fd62e815aefb0519aa0da2313e1c36aa200a5f61a128"}, "tags": {"0.52--hdfd78af_0": "sha256:ffd9cf92a820c25ccc05fd62e815aefb0519aa0da2313e1c36aa200a5f61a128"}, "docker": "quay.io/biocontainers/chexmix", "aliases": {"centrimo-plots": "/usr/local/bin/centrimo-plots", "chexmix": "/usr/local/bin/chexmix", "dtc": "/usr/local/bin/dtc", "fasta-from-bed": "/usr/local/bin/fasta-from-bed", "fasta-holdout-set": "/usr/local/bin/fasta-holdout-set", "fasta-re-match": "/usr/local/bin/fasta-re-match", "index-fasta-file": "/usr/local/bin/index-fasta-file", "meme-chip_html_to_tsv": "/usr/local/bin/meme-chip_html_to_tsv", "momo": "/usr/local/bin/momo", "sea": "/usr/local/bin/sea", "streme": "/usr/local/bin/streme", "streme_xml_to_html": "/usr/local/bin/streme_xml_to_html", "tgene": "/usr/local/bin/tgene", "xstreme": "/usr/local/bin/xstreme", "xstreme_html_to_tsv": "/usr/local/bin/xstreme_html_to_tsv", "alphtype": "/usr/local/bin/alphtype", "ama": "/usr/local/bin/ama", "ama-qvalues": "/usr/local/bin/ama-qvalues", "ame": "/usr/local/bin/ame", "beeml2meme": "/usr/local/bin/beeml2meme", "centrimo": "/usr/local/bin/centrimo", "ceqlogo": "/usr/local/bin/ceqlogo", "chen2meme": "/usr/local/bin/chen2meme", "clustalw2fasta": "/usr/local/bin/clustalw2fasta", "clustalw2phylip": "/usr/local/bin/clustalw2phylip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chexmix.
shpc-registry automated BioContainers addition for chexmix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chexmix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chexmix:0.52--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chexmix/0.52--hdfd78af_0
$ module help quay.io/biocontainers/chexmix/0.52--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chexmix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chexmix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chexmix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chexmix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chexmix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chexmix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### centrimo-plots

```bash
$ singularity exec <container> /usr/local/bin/centrimo-plots
$ podman run --it --rm --entrypoint /usr/local/bin/centrimo-plots   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrimo-plots   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chexmix

```bash
$ singularity exec <container> /usr/local/bin/chexmix
$ podman run --it --rm --entrypoint /usr/local/bin/chexmix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chexmix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dtc

```bash
$ singularity exec <container> /usr/local/bin/dtc
$ podman run --it --rm --entrypoint /usr/local/bin/dtc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dtc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-from-bed

```bash
$ singularity exec <container> /usr/local/bin/fasta-from-bed
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-from-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-from-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-holdout-set

```bash
$ singularity exec <container> /usr/local/bin/fasta-holdout-set
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-holdout-set   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-holdout-set   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### sea

```bash
$ singularity exec <container> /usr/local/bin/sea
$ podman run --it --rm --entrypoint /usr/local/bin/sea   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sea   -v ${PWD} -w ${PWD} <container> -c " $@"
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