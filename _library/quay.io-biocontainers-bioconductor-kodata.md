---
layout: container
name:  "quay.io/biocontainers/bioconductor-kodata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-kodata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-kodata/container.yaml"
updated_at: "2024-10-03 02:57:15.797148"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-kodata"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.23.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-kodata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-kodata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-kodata", "latest": {"1.28.0--r43hdfd78af_0": "sha256:531976f2a1b46f2b6efaa8683b13cef28a1d264d73e64d87e9986da2fa24ee33"}, "tags": {"1.8.0--r351_0": "sha256:fff7b03dc2d0869e147775bfe8cb3e98ff5d59405408b7310935c0a8362b4771", "1.24.0--r42hdfd78af_0": "sha256:c3afd54bc1ffda9437a4c8afbebe3821f9d2dc1920d954cd94c18c6f27daec2f", "1.23.0--r42hdfd78af_0": "sha256:041f9f4c86ea01537cef9d6142903bf6c8923dd2a6e426a0e6cfcb993e44acc3", "1.20.0--r41hdfd78af_1": "sha256:c6ed1a999de43e9cca77755ac66c3e0c7745325aacfb4ca56816fb4d0304426d", "1.18.0--r41hdfd78af_0": "sha256:c436fd753ce0d347c3dd2a2dd6913b58afbb2ece4f214183014f18c7ce294495", "1.16.0--r40hdfd78af_1": "sha256:68ed1ff11eaefacf7db006f6f72a07d463a5776f99b6633d8e122345aa824c42", "1.26.0--r43hdfd78af_0": "sha256:4090dc86211ad94f863b2c5e01d6b5f210a6c9fc2de013e5644fa9c72aead9f2", "1.28.0--r43hdfd78af_0": "sha256:531976f2a1b46f2b6efaa8683b13cef28a1d264d73e64d87e9986da2fa24ee33"}, "docker": "quay.io/biocontainers/bioconductor-kodata", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-kodata.
shpc-registry automated BioContainers addition for bioconductor-kodata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-kodata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-kodata:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-kodata/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-kodata/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-kodata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kodata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kodata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-kodata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-kodata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-kodata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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