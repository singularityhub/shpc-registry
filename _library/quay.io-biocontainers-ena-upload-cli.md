---
layout: container
name:  "quay.io/biocontainers/ena-upload-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ena-upload-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ena-upload-cli/container.yaml"
updated_at: "2025-03-24 03:44:57.301161"
latest: "0.8.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ena-upload-cli"
aliases:
 - "ena-upload-cli"
 - "xml2-config.bak"
 - "normalizer"
 - "xslt-config"
 - "xsltproc"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
versions:
 - "0.6.1--pyh5e36f6f_0"
 - "0.6.2--pyh7cba7a3_0"
 - "0.6.3--pyhdfd78af_0"
 - "0.7.0--pyhdfd78af_0"
 - "0.7.1--pyhdfd78af_0"
 - "0.7.3--pyhdfd78af_0"
 - "0.7.4--pyhdfd78af_0"
 - "0.7.5--pyhdfd78af_0"
 - "0.8.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for ena-upload-cli"
config: {"url": "https://biocontainers.pro/tools/ena-upload-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ena-upload-cli", "latest": {"0.8.0--pyhdfd78af_0": "sha256:56ed9a413cae026b250f0f61162a46bb940e1d42e0b83c9718318a5bc351d507"}, "tags": {"0.6.1--pyh5e36f6f_0": "sha256:b3244a8caf8c18efd7fc7970ed5f79c18b4eeed933be1c488ec90f0741061ca6", "0.6.2--pyh7cba7a3_0": "sha256:4c2b1e5fad9c1d51b04487016f19df04f877606c9b721d53210c2faf8e1fe8e2", "0.6.3--pyhdfd78af_0": "sha256:daefb2a2602122460c0be2e5d62470f7d1c8883c7440cbeb40e513e924ba09a1", "0.7.0--pyhdfd78af_0": "sha256:0326f603885aa049bea28b28fae351f614586e0841ff9a9ad07e70e3b15e2681", "0.7.1--pyhdfd78af_0": "sha256:dd629359417f9407cfb029615884a75dd204854e728708d576b77d05d08ada76", "0.7.3--pyhdfd78af_0": "sha256:5bf7913fd7bc20d9adc3814c1023404a1c4a03cecb172028f86be54fa4b640b0", "0.7.4--pyhdfd78af_0": "sha256:166081a973b43a8e1dce30b7c160c9f8df75bd8d465285dd3c634c3efdbd21fa", "0.7.5--pyhdfd78af_0": "sha256:8c78e6c7eb47b81669e2fe960ab990360c5b2b552254dd6088317f8dae83f6d5", "0.8.0--pyhdfd78af_0": "sha256:56ed9a413cae026b250f0f61162a46bb940e1d42e0b83c9718318a5bc351d507"}, "docker": "quay.io/biocontainers/ena-upload-cli", "aliases": {"ena-upload-cli": "/usr/local/bin/ena-upload-cli", "xml2-config.bak": "/usr/local/bin/xml2-config.bak", "normalizer": "/usr/local/bin/normalizer", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ena-upload-cli.
shpc-registry automated BioContainers addition for ena-upload-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ena-upload-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ena-upload-cli:0.8.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ena-upload-cli/0.8.0--pyhdfd78af_0
$ module help quay.io/biocontainers/ena-upload-cli/0.8.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ena-upload-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ena-upload-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ena-upload-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ena-upload-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ena-upload-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ena-upload-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ena-upload-cli

```bash
$ singularity exec <container> /usr/local/bin/ena-upload-cli
$ podman run --it --rm --entrypoint /usr/local/bin/ena-upload-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ena-upload-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml2-config.bak

```bash
$ singularity exec <container> /usr/local/bin/xml2-config.bak
$ podman run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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