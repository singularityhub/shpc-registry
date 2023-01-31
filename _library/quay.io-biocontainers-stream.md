---
layout: container
name:  "quay.io/biocontainers/stream"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stream/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/stream/container.yaml"
updated_at: "2023-01-31 03:21:31.330838"
latest: "0.4.0--py37r36hc99cbb1_0"
container_url: "https://biocontainers.pro/tools/stream"
aliases:
 - "gunicorn"
 - "slugify"
 - "stream"
 - "stream_run_test"
 - "zip"
 - "unidecode"
 - "jupyter-bundlerextension"
 - "jupyter-nbextension"
 - "jupyter-notebook"
 - "jupyter-serverextension"
 - "unzip"
 - "jupyter-nbconvert"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
versions:
 - "0.4.0--py37r36hc99cbb1_0"
description: "shpc-registry automated BioContainers addition for stream"
config: {"url": "https://biocontainers.pro/tools/stream", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stream", "latest": {"0.4.0--py37r36hc99cbb1_0": "sha256:59ebb094505a21d0fe38825be15c968aeda821dc94bc924080cf799e3a420f0a"}, "tags": {"0.4.0--py37r36hc99cbb1_0": "sha256:59ebb094505a21d0fe38825be15c968aeda821dc94bc924080cf799e3a420f0a"}, "docker": "quay.io/biocontainers/stream", "aliases": {"gunicorn": "/usr/local/bin/gunicorn", "slugify": "/usr/local/bin/slugify", "stream": "/usr/local/bin/stream", "stream_run_test": "/usr/local/bin/stream_run_test", "zip": "/usr/local/bin/zip", "unidecode": "/usr/local/bin/unidecode", "jupyter-bundlerextension": "/usr/local/bin/jupyter-bundlerextension", "jupyter-nbextension": "/usr/local/bin/jupyter-nbextension", "jupyter-notebook": "/usr/local/bin/jupyter-notebook", "jupyter-serverextension": "/usr/local/bin/jupyter-serverextension", "unzip": "/usr/local/bin/unzip", "jupyter-nbconvert": "/usr/local/bin/jupyter-nbconvert", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stream.
shpc-registry automated BioContainers addition for stream
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stream
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stream:0.4.0--py37r36hc99cbb1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stream/0.4.0--py37r36hc99cbb1_0
$ module help quay.io/biocontainers/stream/0.4.0--py37r36hc99cbb1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stream-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stream-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stream-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stream-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stream-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stream-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gunicorn

```bash
$ singularity exec <container> /usr/local/bin/gunicorn
$ podman run --it --rm --entrypoint /usr/local/bin/gunicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slugify

```bash
$ singularity exec <container> /usr/local/bin/slugify
$ podman run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stream

```bash
$ singularity exec <container> /usr/local/bin/stream
$ podman run --it --rm --entrypoint /usr/local/bin/stream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stream_run_test

```bash
$ singularity exec <container> /usr/local/bin/stream_run_test
$ podman run --it --rm --entrypoint /usr/local/bin/stream_run_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stream_run_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zip

```bash
$ singularity exec <container> /usr/local/bin/zip
$ podman run --it --rm --entrypoint /usr/local/bin/zip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unidecode

```bash
$ singularity exec <container> /usr/local/bin/unidecode
$ podman run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-bundlerextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-bundlerextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-notebook

```bash
$ singularity exec <container> /usr/local/bin/jupyter-notebook
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-serverextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-serverextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzip

```bash
$ singularity exec <container> /usr/local/bin/unzip
$ podman run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbconvert

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbconvert
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernel

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernel
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernelspec

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernelspec
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
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