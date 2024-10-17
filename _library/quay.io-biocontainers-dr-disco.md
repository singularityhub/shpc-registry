---
layout: container
name:  "quay.io/biocontainers/dr-disco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dr-disco/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dr-disco/container.yaml"
updated_at: "2024-10-17 03:16:44.733154"
latest: "0.18.3--pyh086e186_0"
container_url: "https://biocontainers.pro/tools/dr-disco"
aliases:
 - "chimerascan-exclude-transcriptome-events"
 - "chimerascan-relative-bedpe-to-CG"
 - "defuse-clusters-to-CG"
 - "dr-disco"
 - "fuma"
 - "fuma-gencode-gtf-to-bed"
 - "fuma-list-to-boolean-list"
 - "fusioncatcher-to-CG"
 - "htseq-count"
 - "htseq-qa"
 - "easy_install-2.7"
 - "qhelpconverter"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
versions:
 - "0.9.0--py27_0"
 - "0.18.0--pyh5ca1d4c_0"
 - "0.16.3--pyh24bf2e0_0"
 - "0.14.0--py27_0"
 - "0.11.0--py27_0"
 - "0.10.0--py27_0"
 - "0.18.3--pyh086e186_0"
description: "shpc-registry automated BioContainers addition for dr-disco"
config: {"url": "https://biocontainers.pro/tools/dr-disco", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dr-disco", "latest": {"0.18.3--pyh086e186_0": "sha256:d756449c8dab37730ef304e11bf57f8ac2a5eacbec0661639aa9d5f92b64e8d3"}, "tags": {"0.9.0--py27_0": "sha256:3c23f84ec053b5ad48a9771ea1946d99d44d71a6c99692f80643f921e26622b3", "0.18.0--pyh5ca1d4c_0": "sha256:9a796b3af392a7fc71c0604199eed8c926f5beea5b6396e4515fc102fb092c38", "0.16.3--pyh24bf2e0_0": "sha256:1002d7fa20fc0b59e43a55e796276043703bb55cc0a95f6a24b960d82022dc42", "0.14.0--py27_0": "sha256:d6864c98592ae65fbf010e4a18b84829ab66f4372f7e9ca8c979a4d3ae57b0ed", "0.11.0--py27_0": "sha256:5c57a6073a008eeb2273f49b2890083ffb564f72c2727f399f9b3e89109fa167", "0.10.0--py27_0": "sha256:172515ed1483f10460bf73d4c9fa8e5be44cd747db230a97813b1d76def9f700", "0.18.3--pyh086e186_0": "sha256:d756449c8dab37730ef304e11bf57f8ac2a5eacbec0661639aa9d5f92b64e8d3"}, "docker": "quay.io/biocontainers/dr-disco", "aliases": {"chimerascan-exclude-transcriptome-events": "/usr/local/bin/chimerascan-exclude-transcriptome-events", "chimerascan-relative-bedpe-to-CG": "/usr/local/bin/chimerascan-relative-bedpe-to-CG", "defuse-clusters-to-CG": "/usr/local/bin/defuse-clusters-to-CG", "dr-disco": "/usr/local/bin/dr-disco", "fuma": "/usr/local/bin/fuma", "fuma-gencode-gtf-to-bed": "/usr/local/bin/fuma-gencode-gtf-to-bed", "fuma-list-to-boolean-list": "/usr/local/bin/fuma-list-to-boolean-list", "fusioncatcher-to-CG": "/usr/local/bin/fusioncatcher-to-CG", "htseq-count": "/usr/local/bin/htseq-count", "htseq-qa": "/usr/local/bin/htseq-qa", "easy_install-2.7": "/usr/local/bin/easy_install-2.7", "qhelpconverter": "/usr/local/bin/qhelpconverter", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dr-disco.
shpc-registry automated BioContainers addition for dr-disco
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dr-disco
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dr-disco:0.18.3--pyh086e186_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dr-disco/0.18.3--pyh086e186_0
$ module help quay.io/biocontainers/dr-disco/0.18.3--pyh086e186_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dr-disco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dr-disco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dr-disco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dr-disco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dr-disco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dr-disco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chimerascan-exclude-transcriptome-events

```bash
$ singularity exec <container> /usr/local/bin/chimerascan-exclude-transcriptome-events
$ podman run --it --rm --entrypoint /usr/local/bin/chimerascan-exclude-transcriptome-events   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chimerascan-exclude-transcriptome-events   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chimerascan-relative-bedpe-to-CG

```bash
$ singularity exec <container> /usr/local/bin/chimerascan-relative-bedpe-to-CG
$ podman run --it --rm --entrypoint /usr/local/bin/chimerascan-relative-bedpe-to-CG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chimerascan-relative-bedpe-to-CG   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### defuse-clusters-to-CG

```bash
$ singularity exec <container> /usr/local/bin/defuse-clusters-to-CG
$ podman run --it --rm --entrypoint /usr/local/bin/defuse-clusters-to-CG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/defuse-clusters-to-CG   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dr-disco

```bash
$ singularity exec <container> /usr/local/bin/dr-disco
$ podman run --it --rm --entrypoint /usr/local/bin/dr-disco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dr-disco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuma

```bash
$ singularity exec <container> /usr/local/bin/fuma
$ podman run --it --rm --entrypoint /usr/local/bin/fuma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuma-gencode-gtf-to-bed

```bash
$ singularity exec <container> /usr/local/bin/fuma-gencode-gtf-to-bed
$ podman run --it --rm --entrypoint /usr/local/bin/fuma-gencode-gtf-to-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuma-gencode-gtf-to-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuma-list-to-boolean-list

```bash
$ singularity exec <container> /usr/local/bin/fuma-list-to-boolean-list
$ podman run --it --rm --entrypoint /usr/local/bin/fuma-list-to-boolean-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuma-list-to-boolean-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fusioncatcher-to-CG

```bash
$ singularity exec <container> /usr/local/bin/fusioncatcher-to-CG
$ podman run --it --rm --entrypoint /usr/local/bin/fusioncatcher-to-CG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fusioncatcher-to-CG   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-count

```bash
$ singularity exec <container> /usr/local/bin/htseq-count
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-qa

```bash
$ singularity exec <container> /usr/local/bin/htseq-qa
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-2.7

```bash
$ singularity exec <container> /usr/local/bin/easy_install-2.7
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-roh.pl

```bash
$ singularity exec <container> /usr/local/bin/run-roh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-vcfstats

```bash
$ singularity exec <container> /usr/local/bin/plot-vcfstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
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