---
layout: container
name:  "quay.io/biocontainers/clinvar-this"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clinvar-this/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clinvar-this/container.yaml"
updated_at: "2023-11-28 03:10:19.423018"
latest: "0.12.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/clinvar-this"
aliases:
 - "clinvar-this"
 - "tabulate"
 - "jsonschema"
 - "normalizer"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.1.0--pyhdfd78af_0"
 - "0.2.1--pyhdfd78af_0"
 - "0.10.2--pyhdfd78af_0"
 - "0.7.0--pyhdfd78af_0"
 - "0.6.0--pyhdfd78af_0"
 - "0.4.1--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "0.12.0--pyhdfd78af_0"
 - "0.11.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for clinvar-this"
config: {"url": "https://biocontainers.pro/tools/clinvar-this", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for clinvar-this", "latest": {"0.12.0--pyhdfd78af_0": "sha256:5668dcaac9a194d5bc63c21454487f13c300e13aaad0edfcbc2ff77e172cd561"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:12cb7a7947769f54ad7bebdc328664272c8b0e9d89eb5db7edfe9bb5ad3ba5f9", "0.2.1--pyhdfd78af_0": "sha256:e008e028dd2386aa919c8fefdba82d5e19d6f10a15f9f33c9803dcec3a150293", "0.10.2--pyhdfd78af_0": "sha256:b4805af60693d5b20f8c9f6d50eaee9b0b61d72cecf05ee724c616100e9ac413", "0.7.0--pyhdfd78af_0": "sha256:92501bb2e685069b0954920e7362504bf127fec85d8355b0ad122c8d7bc9386b", "0.6.0--pyhdfd78af_0": "sha256:1c77bd81dd73dc0771e4da322306687b3d11918ee95b2af5254bf26e98920868", "0.4.1--pyhdfd78af_0": "sha256:c22ba00c56620014b227f21b00a9cfacb40ab3276d1683579322735322618cba", "0.3.0--pyhdfd78af_0": "sha256:c4f85b754dcd80898d3989126a26dd8e4d4ed493962265768b4d293cff405b02", "0.12.0--pyhdfd78af_0": "sha256:5668dcaac9a194d5bc63c21454487f13c300e13aaad0edfcbc2ff77e172cd561", "0.11.0--pyhdfd78af_0": "sha256:7d863e934d8c27a8d17d6ae634eaab362521f1f97c859f65dc35e5e8eee7e7b6"}, "docker": "quay.io/biocontainers/clinvar-this", "aliases": {"clinvar-this": "/usr/local/bin/clinvar-this", "tabulate": "/usr/local/bin/tabulate", "jsonschema": "/usr/local/bin/jsonschema", "normalizer": "/usr/local/bin/normalizer", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clinvar-this.
singularity registry hpc automated addition for clinvar-this
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clinvar-this
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clinvar-this:0.12.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clinvar-this/0.12.0--pyhdfd78af_0
$ module help quay.io/biocontainers/clinvar-this/0.12.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clinvar-this-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clinvar-this-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clinvar-this-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clinvar-this-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clinvar-this-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clinvar-this-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clinvar-this

```bash
$ singularity exec <container> /usr/local/bin/clinvar-this
$ podman run --it --rm --entrypoint /usr/local/bin/clinvar-this   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clinvar-this   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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