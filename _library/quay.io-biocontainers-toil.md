---
layout: container
name:  "quay.io/biocontainers/toil"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/toil/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/toil/container.yaml"
updated_at: "2022-10-27 01:03:25.063101"
latest: "5.6.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/toil"
aliases:
 - "_toil_contained_executor"
 - "_toil_mesos_executor"
 - "_toil_worker"
 - "cwltoil"
 - "toil"
 - "toil-cwl-runner"
 - "wsdump"
versions:
 - "5.6.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for toil"
config: {"url": "https://biocontainers.pro/tools/toil", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for toil", "latest": {"5.6.0--pyhdfd78af_0": "sha256:d148c547f7829b59b69155dd5add29ddd2d8a3b93e10f3f9ebbdb1126bc63041"}, "tags": {"5.6.0--pyhdfd78af_0": "sha256:d148c547f7829b59b69155dd5add29ddd2d8a3b93e10f3f9ebbdb1126bc63041"}, "docker": "quay.io/biocontainers/toil", "aliases": {"_toil_contained_executor": "/usr/local/bin/_toil_contained_executor", "_toil_mesos_executor": "/usr/local/bin/_toil_mesos_executor", "_toil_worker": "/usr/local/bin/_toil_worker", "cwltoil": "/usr/local/bin/cwltoil", "toil": "/usr/local/bin/toil", "toil-cwl-runner": "/usr/local/bin/toil-cwl-runner", "wsdump": "/usr/local/bin/wsdump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/toil.
shpc-registry automated BioContainers addition for toil
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/toil
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/toil:5.6.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/toil/5.6.0--pyhdfd78af_0
$ module help quay.io/biocontainers/toil/5.6.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### toil-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### toil-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### toil-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### toil-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### toil-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### toil-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### _toil_contained_executor

```bash
$ singularity exec <container> /usr/local/bin/_toil_contained_executor
$ podman run --it --rm --entrypoint /usr/local/bin/_toil_contained_executor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_toil_contained_executor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _toil_mesos_executor

```bash
$ singularity exec <container> /usr/local/bin/_toil_mesos_executor
$ podman run --it --rm --entrypoint /usr/local/bin/_toil_mesos_executor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_toil_mesos_executor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _toil_worker

```bash
$ singularity exec <container> /usr/local/bin/_toil_worker
$ podman run --it --rm --entrypoint /usr/local/bin/_toil_worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_toil_worker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwltoil

```bash
$ singularity exec <container> /usr/local/bin/cwltoil
$ podman run --it --rm --entrypoint /usr/local/bin/cwltoil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwltoil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toil

```bash
$ singularity exec <container> /usr/local/bin/toil
$ podman run --it --rm --entrypoint /usr/local/bin/toil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toil-cwl-runner

```bash
$ singularity exec <container> /usr/local/bin/toil-cwl-runner
$ podman run --it --rm --entrypoint /usr/local/bin/toil-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toil-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
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