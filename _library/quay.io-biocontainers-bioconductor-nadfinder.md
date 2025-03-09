---
layout: container
name:  "quay.io/biocontainers/bioconductor-nadfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nadfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nadfinder/container.yaml"
updated_at: "2025-03-09 03:20:17.732767"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nadfinder"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nadfinder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nadfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nadfinder", "latest": {"1.30.0--r44hdfd78af_0": "sha256:b6b694a8f98ed483a577a9f0cb49ca135033f43596e44c02922b0908dfd3eafc"}, "tags": {"1.8.1--r36_0": "sha256:11477deba3fc8e79926acd97031d0fa1b55623213a6cde33fbc52e56fc930754", "1.22.0--r42hdfd78af_0": "sha256:c09ae1a1d67101b4751b3cf4963e7f34652c3bdc47802e2749c3a3e474da7627", "1.18.0--r41hdfd78af_0": "sha256:fd262d09d3246fb832a678560b656eeafb99ead6ed823c836aef3dd628a23700", "1.16.0--r41hdfd78af_0": "sha256:b7474e5410e73a998937e3e9403b3dac8fde7f7ffa79ce02a480acfc82083b07", "1.14.0--r40hdfd78af_1": "sha256:4ce1d440c5b6fe2f2e42830b1860ba545cca03c0cab417161cae63e04eb8e493", "1.12.0--r40_0": "sha256:9ee498f532fd22ef3ca22c9c24ddd39fe6d4349d9620f11089024abee5c81b66", "1.24.0--r43hdfd78af_0": "sha256:3a60814e4852ff4ed95d2d9c48a5b0c1f98324ab6c866458130d8d5ef0eec54f", "1.26.0--r43hdfd78af_0": "sha256:52b75e459984a23a43cf49eec5b2dd53dffe35e5ce7ef07574cf81de2c3897af", "1.30.0--r44hdfd78af_0": "sha256:b6b694a8f98ed483a577a9f0cb49ca135033f43596e44c02922b0908dfd3eafc"}, "docker": "quay.io/biocontainers/bioconductor-nadfinder", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nadfinder.
shpc-registry automated BioContainers addition for bioconductor-nadfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nadfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nadfinder:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nadfinder/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nadfinder/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nadfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nadfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nadfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nadfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nadfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nadfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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