---
layout: container
name:  "quay.io/biocontainers/sequnwinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sequnwinder/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sequnwinder/container.yaml"
updated_at: "2022-10-27 01:01:39.162451"
latest: "0.1.4--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/sequnwinder"
aliases:
 - "dtc"
 - "enr"
 - "fasta-from-bed"
 - "index-fasta-file"
 - "sequnwinder"
 - "streme"
 - "streme_xml_to_html"
 - "tgene"
versions:
 - "0.1.4--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for sequnwinder"
config: {"url": "https://biocontainers.pro/tools/sequnwinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sequnwinder", "latest": {"0.1.4--hdfd78af_1": "sha256:8cc85e27130f2aec854d4aafc10596a2159bf17bb28647c80d82faf89f7b1c5c"}, "tags": {"0.1.4--hdfd78af_1": "sha256:8cc85e27130f2aec854d4aafc10596a2159bf17bb28647c80d82faf89f7b1c5c"}, "docker": "quay.io/biocontainers/sequnwinder", "aliases": {"dtc": "/usr/local/bin/dtc", "enr": "/usr/local/bin/enr", "fasta-from-bed": "/usr/local/bin/fasta-from-bed", "index-fasta-file": "/usr/local/bin/index-fasta-file", "sequnwinder": "/usr/local/bin/sequnwinder", "streme": "/usr/local/bin/streme", "streme_xml_to_html": "/usr/local/bin/streme_xml_to_html", "tgene": "/usr/local/bin/tgene"}}
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


#### index-fasta-file

```bash
$ singularity exec <container> /usr/local/bin/index-fasta-file
$ podman run --it --rm --entrypoint /usr/local/bin/index-fasta-file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-fasta-file   -v ${PWD} -w ${PWD} <container> -c " $@"
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