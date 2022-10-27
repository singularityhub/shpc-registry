---
layout: container
name:  "quay.io/biocontainers/gcs-oauth2-boto-plugin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gcs-oauth2-boto-plugin/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gcs-oauth2-boto-plugin/container.yaml"
updated_at: "2022-10-27 01:16:02.968259"
latest: "1.9--py27_1"
container_url: "https://biocontainers.pro/tools/gcs-oauth2-boto-plugin"

versions:
 - "1.9--py27_1"
description: "shpc-registry automated BioContainers addition for gcs-oauth2-boto-plugin"
config: {"url": "https://biocontainers.pro/tools/gcs-oauth2-boto-plugin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gcs-oauth2-boto-plugin", "latest": {"1.9--py27_1": "sha256:9cdca061449225c40d6296fbd3d992c4517104996d6c2f88dbc2f7ddb0254791"}, "tags": {"1.9--py27_1": "sha256:9cdca061449225c40d6296fbd3d992c4517104996d6c2f88dbc2f7ddb0254791"}, "docker": "quay.io/biocontainers/gcs-oauth2-boto-plugin"}
---

This module is a singularity container wrapper for quay.io/biocontainers/gcs-oauth2-boto-plugin.
shpc-registry automated BioContainers addition for gcs-oauth2-boto-plugin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gcs-oauth2-boto-plugin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gcs-oauth2-boto-plugin:1.9--py27_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gcs-oauth2-boto-plugin/1.9--py27_1
$ module help quay.io/biocontainers/gcs-oauth2-boto-plugin/1.9--py27_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gcs-oauth2-boto-plugin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gcs-oauth2-boto-plugin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gcs-oauth2-boto-plugin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gcs-oauth2-boto-plugin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gcs-oauth2-boto-plugin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gcs-oauth2-boto-plugin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### gcs-oauth2-boto-plugin

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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