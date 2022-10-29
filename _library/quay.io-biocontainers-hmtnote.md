---
layout: container
name:  "quay.io/biocontainers/hmtnote"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmtnote/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hmtnote/container.yaml"
updated_at: "2022-10-29 05:52:27.240017"
latest: "0.7.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/hmtnote"
aliases:
 - "hmtnote"
 - "bokeh"
 - "brotli"
 - "cwebp"
 - "dask-scheduler"
 - "dask-ssh"
 - "dask-worker"
 - "dwebp"
 - "f2py3.9"
 - "fonttools"
 - "gif2h5"
versions:
 - "0.7.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for hmtnote"
config: {"url": "https://biocontainers.pro/tools/hmtnote", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmtnote", "latest": {"0.7.2--pyhdfd78af_0": "sha256:330c0c5c07e1a4785aa99a6a7ba1f98095e70051367626892d80714b65a79f71"}, "tags": {"0.7.2--pyhdfd78af_0": "sha256:330c0c5c07e1a4785aa99a6a7ba1f98095e70051367626892d80714b65a79f71"}, "docker": "quay.io/biocontainers/hmtnote", "aliases": {"hmtnote": "/usr/local/bin/hmtnote", "bokeh": "/usr/local/bin/bokeh", "brotli": "/usr/local/bin/brotli", "cwebp": "/usr/local/bin/cwebp", "dask-scheduler": "/usr/local/bin/dask-scheduler", "dask-ssh": "/usr/local/bin/dask-ssh", "dask-worker": "/usr/local/bin/dask-worker", "dwebp": "/usr/local/bin/dwebp", "f2py3.9": "/usr/local/bin/f2py3.9", "fonttools": "/usr/local/bin/fonttools", "gif2h5": "/usr/local/bin/gif2h5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmtnote.
shpc-registry automated BioContainers addition for hmtnote
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmtnote
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmtnote:0.7.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmtnote/0.7.2--pyhdfd78af_0
$ module help quay.io/biocontainers/hmtnote/0.7.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmtnote-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmtnote-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmtnote-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmtnote-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmtnote-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmtnote-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hmtnote

```bash
$ singularity exec <container> /usr/local/bin/hmtnote
$ podman run --it --rm --entrypoint /usr/local/bin/hmtnote   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmtnote   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bokeh

```bash
$ singularity exec <container> /usr/local/bin/bokeh
$ podman run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-scheduler

```bash
$ singularity exec <container> /usr/local/bin/dask-scheduler
$ podman run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-ssh

```bash
$ singularity exec <container> /usr/local/bin/dask-ssh
$ podman run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-worker

```bash
$ singularity exec <container> /usr/local/bin/dask-worker
$ podman run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwebp

```bash
$ singularity exec <container> /usr/local/bin/dwebp
$ podman run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
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