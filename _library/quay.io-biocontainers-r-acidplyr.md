---
layout: container
name:  "quay.io/biocontainers/r-acidplyr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-acidplyr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-acidplyr/container.yaml"
updated_at: "2024-11-16 03:10:48.905567"
latest: "0.5.4--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-acidplyr"

versions:
 - "0.2.0--r41hdfd78af_0"
 - "0.2.0--r41hdfd78af_1"
 - "0.3.2--r42hdfd78af_1"
 - "0.3.4--r42hdfd78af_0"
 - "0.3.7--r42hdfd78af_1"
 - "0.3.10--r42hdfd78af_1"
 - "0.3.10--r43hdfd78af_2"
 - "0.4.2--r43hdfd78af_0"
 - "0.3.11--r43hdfd78af_0"
 - "0.5.0--r43hdfd78af_0"
 - "0.5.1--r43hdfd78af_0"
 - "0.5.2--r43hdfd78af_0"
 - "0.5.3--r43hdfd78af_0"
 - "0.5.4--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-acidplyr"
config: {"url": "https://biocontainers.pro/tools/r-acidplyr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-acidplyr", "latest": {"0.5.4--r43hdfd78af_0": "sha256:d789c2bff7855a7605d24a4c80c6e6c1036a607aef6d7b7dfdcad5757c13cfb7"}, "tags": {"0.2.0--r41hdfd78af_0": "sha256:3d3d96c8325669aa2724e505f174ed2e4aa957c6e0ef174d6289b1b7c8b52cd1", "0.2.0--r41hdfd78af_1": "sha256:c9c8ad610a9cc354fa3cfb93b0a46623d6d7431b1113ce6fe5d6507b20b88c50", "0.3.2--r42hdfd78af_1": "sha256:34643d02cad183deda70e12255bc25b5ae54be1eceb4d2261e43fd9c15a9e8dc", "0.3.4--r42hdfd78af_0": "sha256:9bf6fe2caa96d874f20f3531e85e8e23e749e84b87f0ac8e7429962e7c75973b", "0.3.7--r42hdfd78af_1": "sha256:743d49ed08fa919dbeee76df024bc656920e7146959f777323757c8b050f4eb3", "0.3.10--r42hdfd78af_1": "sha256:f3a746f5dbfea6b36e0a2e9b4cdce87667cd26a129de61045b67eaffe74b2e7d", "0.3.10--r43hdfd78af_2": "sha256:95492aa44a4ceba03e0d336ba69d106a421bb52247a3f2f2c935992954032c27", "0.4.2--r43hdfd78af_0": "sha256:5636502ff7dcb9813235f11a3d25cc79171650534a0c11b236fe6e5989c31446", "0.3.11--r43hdfd78af_0": "sha256:ab6eb18e742e8cb0230d29fa4c1cb9461b1c1134d8b712660d735770ede019cc", "0.5.0--r43hdfd78af_0": "sha256:ecfe591d920496de5612388a29c1aa09bcbc42f26db5cc328cedc1e5fc73566c", "0.5.1--r43hdfd78af_0": "sha256:a7649a5854b995b721366a0b97e1433cf1261a5b6e72a65486552db906c5ace8", "0.5.2--r43hdfd78af_0": "sha256:e17d7f37dc9d35bee31370c4c99b548d2178f4434ce0916bd7680e8d2e975cbb", "0.5.3--r43hdfd78af_0": "sha256:ef78a9a070a487db67b4a12856789003a009776422f61470117efe33f79cb3e1", "0.5.4--r43hdfd78af_0": "sha256:d789c2bff7855a7605d24a4c80c6e6c1036a607aef6d7b7dfdcad5757c13cfb7"}, "docker": "quay.io/biocontainers/r-acidplyr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-acidplyr.
shpc-registry automated BioContainers addition for r-acidplyr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-acidplyr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-acidplyr:0.5.4--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-acidplyr/0.5.4--r43hdfd78af_0
$ module help quay.io/biocontainers/r-acidplyr/0.5.4--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-acidplyr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-acidplyr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-acidplyr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-acidplyr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-acidplyr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-acidplyr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-acidplyr

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