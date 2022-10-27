---
layout: container
name:  "quay.io/biocontainers/metavelvet-sl-feature-extraction"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metavelvet-sl-feature-extraction/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metavelvet-sl-feature-extraction/container.yaml"
updated_at: "2022-10-27 00:48:17.005201"
latest: "1.0--pl526_3"
container_url: "https://biocontainers.pro/tools/metavelvet-sl-feature-extraction"
aliases:
 - "FeatureExtract.pl"
 - "FeatureExtractPredict.pl"
 - "eval.pl"
versions:
 - "1.0--pl526_3"
description: "shpc-registry automated BioContainers addition for metavelvet-sl-feature-extraction"
config: {"url": "https://biocontainers.pro/tools/metavelvet-sl-feature-extraction", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metavelvet-sl-feature-extraction", "latest": {"1.0--pl526_3": "sha256:bc42275b009c84d2272a6db13e6dd65b147677baf4bfb8c593b8f34ef8c465df"}, "tags": {"1.0--pl526_3": "sha256:bc42275b009c84d2272a6db13e6dd65b147677baf4bfb8c593b8f34ef8c465df"}, "docker": "quay.io/biocontainers/metavelvet-sl-feature-extraction", "aliases": {"FeatureExtract.pl": "/usr/local/bin/FeatureExtract.pl", "FeatureExtractPredict.pl": "/usr/local/bin/FeatureExtractPredict.pl", "eval.pl": "/usr/local/bin/eval.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metavelvet-sl-feature-extraction.
shpc-registry automated BioContainers addition for metavelvet-sl-feature-extraction
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metavelvet-sl-feature-extraction
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metavelvet-sl-feature-extraction:1.0--pl526_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metavelvet-sl-feature-extraction/1.0--pl526_3
$ module help quay.io/biocontainers/metavelvet-sl-feature-extraction/1.0--pl526_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metavelvet-sl-feature-extraction-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metavelvet-sl-feature-extraction-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metavelvet-sl-feature-extraction-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metavelvet-sl-feature-extraction-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metavelvet-sl-feature-extraction-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metavelvet-sl-feature-extraction-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FeatureExtract.pl

```bash
$ singularity exec <container> /usr/local/bin/FeatureExtract.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FeatureExtract.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FeatureExtract.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FeatureExtractPredict.pl

```bash
$ singularity exec <container> /usr/local/bin/FeatureExtractPredict.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FeatureExtractPredict.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FeatureExtractPredict.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eval.pl

```bash
$ singularity exec <container> /usr/local/bin/eval.pl
$ podman run --it --rm --entrypoint /usr/local/bin/eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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