---
layout: container
name:  "quay.io/biocontainers/bioconductor-openprimerui"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-openprimerui/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-openprimerui/container.yaml"
updated_at: "2023-01-22 03:18:22.816791"
latest: "1.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-openprimerui"
aliases:
 - "mafft-sparsecore.rb"
 - "pandoc-citeproc"
 - "einsi"
 - "fftns"
 - "fftnsi"
 - "ginsi"
 - "linsi"
 - "mafft-distance"
 - "mafft-einsi"
 - "mafft-fftns"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-openprimerui"
config: {"url": "https://biocontainers.pro/tools/bioconductor-openprimerui", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-openprimerui", "latest": {"1.20.0--r42hdfd78af_0": "sha256:a03936a2797f1ce440137809f8b847df8cd628bebe8665ee1edd05288ff93d80"}, "tags": {"1.8.0--r36_0": "sha256:5ec0ba47e4cdedd07e07f99605916a073395a0ba7c9afa21d22d39c439a6d44c", "1.20.0--r42hdfd78af_0": "sha256:a03936a2797f1ce440137809f8b847df8cd628bebe8665ee1edd05288ff93d80", "1.16.0--r41hdfd78af_0": "sha256:1e4a752208e9c831074a58018c9e29123d855c38aa3a15565ac8f94c9d15b0ec", "1.14.0--r41hdfd78af_0": "sha256:5cf7c59dca782875d524135ac5c31fd4690ba34f30f20843e7e90e1faf4d643a", "1.12.0--r40hdfd78af_1": "sha256:5acbaa4c59955d7ae9501d68d5670c58fc0641d8b813f2f6d4504899726f8fd5", "1.10.0--r40_0": "sha256:8bfcbd6a88c0574e2e31d52ad4a867875e1f262784fc92ca74fac7b2940a0cdb"}, "docker": "quay.io/biocontainers/bioconductor-openprimerui", "aliases": {"mafft-sparsecore.rb": "/usr/local/bin/mafft-sparsecore.rb", "pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "einsi": "/usr/local/bin/einsi", "fftns": "/usr/local/bin/fftns", "fftnsi": "/usr/local/bin/fftnsi", "ginsi": "/usr/local/bin/ginsi", "linsi": "/usr/local/bin/linsi", "mafft-distance": "/usr/local/bin/mafft-distance", "mafft-einsi": "/usr/local/bin/mafft-einsi", "mafft-fftns": "/usr/local/bin/mafft-fftns"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-openprimerui.
shpc-registry automated BioContainers addition for bioconductor-openprimerui
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-openprimerui
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-openprimerui:1.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-openprimerui/1.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-openprimerui/1.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-openprimerui-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-openprimerui-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-openprimerui-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-openprimerui-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-openprimerui-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-openprimerui-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mafft-sparsecore.rb

```bash
$ singularity exec <container> /usr/local/bin/mafft-sparsecore.rb
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### einsi

```bash
$ singularity exec <container> /usr/local/bin/einsi
$ podman run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftns

```bash
$ singularity exec <container> /usr/local/bin/fftns
$ podman run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftnsi

```bash
$ singularity exec <container> /usr/local/bin/fftnsi
$ podman run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ginsi

```bash
$ singularity exec <container> /usr/local/bin/ginsi
$ podman run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linsi

```bash
$ singularity exec <container> /usr/local/bin/linsi
$ podman run --it --rm --entrypoint /usr/local/bin/linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-distance

```bash
$ singularity exec <container> /usr/local/bin/mafft-distance
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-einsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-einsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-fftns

```bash
$ singularity exec <container> /usr/local/bin/mafft-fftns
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
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