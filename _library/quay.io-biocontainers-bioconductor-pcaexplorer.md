---
layout: container
name:  "quay.io/biocontainers/bioconductor-pcaexplorer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pcaexplorer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pcaexplorer/container.yaml"
updated_at: "2025-09-27 03:04:03.790669"
latest: "3.0.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pcaexplorer"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r351_0"
 - "2.24.0--r42hdfd78af_0"
 - "2.20.0--r41hdfd78af_0"
 - "2.18.0--r41hdfd78af_0"
 - "2.16.0--r40hdfd78af_1"
 - "2.14.0--r40_0"
 - "2.26.1--r43hdfd78af_0"
 - "2.28.0--r43hdfd78af_0"
 - "3.0.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pcaexplorer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pcaexplorer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pcaexplorer", "latest": {"3.0.0--r44hdfd78af_0": "sha256:f90cde8de3393e4778e480e9b210f1742607305b8b15d7ff0b069b163b5578a6"}, "tags": {"2.8.0--r351_0": "sha256:cbf0443273a9c61bbd917a2851b210351d6fbedc539fb5e0e2fa3c3e6541dfe1", "2.24.0--r42hdfd78af_0": "sha256:cc221554cd8dd5e71e6e9d46017a94b0aa0183d487ee7806ca5f6ef97fffd8e2", "2.20.0--r41hdfd78af_0": "sha256:bbcaaf83e21662be577c519c5fb8c85c777ada6874a0db340c494d2404aac076", "2.18.0--r41hdfd78af_0": "sha256:051a5650c2eb34392bb241d089c7abb9b8e033ecf648969759bdc50452254f3e", "2.16.0--r40hdfd78af_1": "sha256:8fab6a96acf7262d9a3070abcf3151797565facd05985f8e94005d9e90e40864", "2.14.0--r40_0": "sha256:f04707b1f8338e573729defde3522c6368513ba3d41c9163f5133187115300f8", "2.26.1--r43hdfd78af_0": "sha256:038ed53794753cce0274ff3458f9a204036e4c47fdc59ed6f90770eacb98b957", "2.28.0--r43hdfd78af_0": "sha256:811ca985d1693ff98814034310db0179fabcf16dcbb9fd4aa135712129b0bee0", "3.0.0--r44hdfd78af_0": "sha256:f90cde8de3393e4778e480e9b210f1742607305b8b15d7ff0b069b163b5578a6"}, "docker": "quay.io/biocontainers/bioconductor-pcaexplorer", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pcaexplorer.
shpc-registry automated BioContainers addition for bioconductor-pcaexplorer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pcaexplorer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pcaexplorer:3.0.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pcaexplorer/3.0.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pcaexplorer/3.0.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pcaexplorer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pcaexplorer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pcaexplorer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pcaexplorer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pcaexplorer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pcaexplorer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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