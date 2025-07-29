---
layout: container
name:  "quay.io/biocontainers/bioconductor-intact"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-intact/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-intact/container.yaml"
updated_at: "2025-07-29 04:21:35.077170"
latest: "1.6.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-intact"
aliases:
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.1--r43hdfd78af_0"
 - "1.2.0--r43hdfd78af_0"
 - "1.6.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-intact"
config: {"url": "https://biocontainers.pro/tools/bioconductor-intact", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-intact", "latest": {"1.6.0--r44hdfd78af_0": "sha256:c5f06b9ee6daeea55da80fc0d57e366ccb393eac764fa786f2ff881aee329899"}, "tags": {"1.0.1--r43hdfd78af_0": "sha256:bb6ff4b3198c3f05cb1b447bc38ec402ad8eec7475df73cb369896c09c048def", "1.2.0--r43hdfd78af_0": "sha256:ba26e677bb3b5e561d99803177d1dae6078d5e1f84d5c75a2a35d93d6dbc1537", "1.6.0--r44hdfd78af_0": "sha256:c5f06b9ee6daeea55da80fc0d57e366ccb393eac764fa786f2ff881aee329899"}, "docker": "quay.io/biocontainers/bioconductor-intact", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-intact.
singularity registry hpc automated addition for bioconductor-intact
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-intact
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-intact:1.6.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-intact/1.6.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-intact/1.6.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-intact-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-intact-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-intact-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-intact-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-intact-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-intact-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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