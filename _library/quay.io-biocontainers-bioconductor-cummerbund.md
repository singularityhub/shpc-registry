---
layout: container
name:  "quay.io/biocontainers/bioconductor-cummerbund"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cummerbund/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cummerbund/container.yaml"
updated_at: "2025-11-27 03:31:33.024516"
latest: "2.48.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cummerbund"
aliases:
 - "wget"
versions:
 - "2.8.2--r351_1"
 - "2.36.0--r41hdfd78af_0"
 - "2.34.0--r41hdfd78af_0"
 - "2.32.0--r40hdfd78af_1"
 - "2.30.0--r40_0"
 - "2.28.0--r36_0"
 - "2.40.0--r42hdfd78af_0"
 - "2.42.0--r43hdfd78af_0"
 - "2.44.0--r43hdfd78af_0"
 - "2.48.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cummerbund"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cummerbund", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cummerbund", "latest": {"2.48.0--r44hdfd78af_0": "sha256:f5e4cda8e320f9ef5ef200d038d95518f352d7788d75ceb6b31691e0038a3673"}, "tags": {"2.8.2--r351_1": "sha256:844ff52c9bade4940b7b983c6bcf47b1ef4ad19d8b6e740b1709b96cc898771d", "2.36.0--r41hdfd78af_0": "sha256:53af8aff39f4fc24aea92bbb105a8f0a37361b617c1cfc5ca9e4f093aa8bac25", "2.34.0--r41hdfd78af_0": "sha256:57a2c9b3db144c29a1be7fb5a09f2e8afe9780cede99f69582054ed78ce15b3d", "2.32.0--r40hdfd78af_1": "sha256:0bb80bab5e93fd9f2cf3c8eaf9d87ba353a5b2b25a7320325526a31808c6c820", "2.30.0--r40_0": "sha256:9a1430d93617a914133a61f6d3cc1a6742c0edc66fcf2d5a18835a1cb27025f1", "2.28.0--r36_0": "sha256:9cde3e069afe675cac49a960c9a885524cdbc05fcf5653c018cccd987a39418c", "2.40.0--r42hdfd78af_0": "sha256:c3178b2112fe1ec353a1d3cbf4ef8ab2c186f286d72197839e3d41f0d759acb8", "2.42.0--r43hdfd78af_0": "sha256:2941a1c5d911e94fd0576cadd3ddf468947c65238df8de736f9d2c2cf7bac805", "2.44.0--r43hdfd78af_0": "sha256:a82ddb8fe0a0b695686ae2466a71283921cfa149854b72c837d566a35c75b40f", "2.48.0--r44hdfd78af_0": "sha256:f5e4cda8e320f9ef5ef200d038d95518f352d7788d75ceb6b31691e0038a3673"}, "docker": "quay.io/biocontainers/bioconductor-cummerbund", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cummerbund.
shpc-registry automated BioContainers addition for bioconductor-cummerbund
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cummerbund
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cummerbund:2.48.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cummerbund/2.48.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cummerbund/2.48.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cummerbund-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cummerbund-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cummerbund-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cummerbund-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cummerbund-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cummerbund-inspect-deffile:

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