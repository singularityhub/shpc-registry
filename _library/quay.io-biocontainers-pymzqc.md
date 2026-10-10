---
layout: container
name:  "quay.io/biocontainers/pymzqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pymzqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pymzqc/container.yaml"
updated_at: "2026-10-10 18:56:04.188646"
latest: "1.0.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pymzqc"
aliases:
 - "mzqc-fileinfo"
 - "mzqc-filemerger"
 - "mzqc-fixdescriptions"
 - "mzqc-validator"
 - "idna"
 - "chardetect"
 - "jsonschema"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "numpy-config"
 - "normalizer"
versions:
 - "1.0.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pymzqc"
config: {"url": "https://biocontainers.pro/tools/pymzqc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pymzqc", "latest": {"1.0.3--pyhdfd78af_0": "sha256:d9e2629b2b0d1c88a5bd681b7939e36152e1e81d2bab33d602b43d86cab75df2"}, "tags": {"1.0.3--pyhdfd78af_0": "sha256:d9e2629b2b0d1c88a5bd681b7939e36152e1e81d2bab33d602b43d86cab75df2"}, "docker": "quay.io/biocontainers/pymzqc", "aliases": {"mzqc-fileinfo": "/usr/local/bin/mzqc-fileinfo", "mzqc-filemerger": "/usr/local/bin/mzqc-filemerger", "mzqc-fixdescriptions": "/usr/local/bin/mzqc-fixdescriptions", "mzqc-validator": "/usr/local/bin/mzqc-validator", "idna": "/usr/local/bin/idna", "chardetect": "/usr/local/bin/chardetect", "jsonschema": "/usr/local/bin/jsonschema", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "numpy-config": "/usr/local/bin/numpy-config", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pymzqc.
singularity registry hpc automated addition for pymzqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pymzqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pymzqc:1.0.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pymzqc/1.0.3--pyhdfd78af_0
$ module help quay.io/biocontainers/pymzqc/1.0.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pymzqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pymzqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pymzqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pymzqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pymzqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pymzqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mzqc-fileinfo

```bash
$ singularity exec <container> /usr/local/bin/mzqc-fileinfo
$ podman run --it --rm --entrypoint /usr/local/bin/mzqc-fileinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mzqc-fileinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mzqc-filemerger

```bash
$ singularity exec <container> /usr/local/bin/mzqc-filemerger
$ podman run --it --rm --entrypoint /usr/local/bin/mzqc-filemerger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mzqc-filemerger   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mzqc-fixdescriptions

```bash
$ singularity exec <container> /usr/local/bin/mzqc-fixdescriptions
$ podman run --it --rm --entrypoint /usr/local/bin/mzqc-fixdescriptions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mzqc-fixdescriptions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mzqc-validator

```bash
$ singularity exec <container> /usr/local/bin/mzqc-validator
$ podman run --it --rm --entrypoint /usr/local/bin/mzqc-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mzqc-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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