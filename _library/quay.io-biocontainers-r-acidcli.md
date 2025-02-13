---
layout: container
name:  "quay.io/biocontainers/r-acidcli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-acidcli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-acidcli/container.yaml"
updated_at: "2025-02-13 02:51:33.320051"
latest: "0.3.0--r44hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-acidcli"

versions:
 - "0.2.0--r41hdfd78af_0"
 - "0.2.5--r42hdfd78af_0"
 - "0.2.5--r42hdfd78af_1"
 - "0.2.7--r42hdfd78af_0"
 - "0.2.7--r42hdfd78af_1"
 - "0.2.8--r43hdfd78af_0"
 - "0.3.0--r43hdfd78af_0"
 - "0.3.0--r44hdfd78af_1"
description: "shpc-registry automated BioContainers addition for r-acidcli"
config: {"url": "https://biocontainers.pro/tools/r-acidcli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-acidcli", "latest": {"0.3.0--r44hdfd78af_1": "sha256:63026fff7df18176f26d3c727837cf084632224b99a1c6644d8a90c25bb883f5"}, "tags": {"0.2.0--r41hdfd78af_0": "sha256:9a36d78a939ef97ccaa9ecdc4f7f9873c5af3155c740e1e18fb20f74acd54a2e", "0.2.5--r42hdfd78af_0": "sha256:8af160273025875429f3318b9e6fe69a6cc05df3616b02e74ba8d6a16c4e0b94", "0.2.5--r42hdfd78af_1": "sha256:63db18130bc765abfc42ed08eb9770bd9765bf09a908dd8585aca000892f9f01", "0.2.7--r42hdfd78af_0": "sha256:62dbf9f522d4950e4a8e87b0c96715619f4207cf1d62a3e59aa3259f4f789c6c", "0.2.7--r42hdfd78af_1": "sha256:04156c07eb788ff9d13fbf8d730ebacb1faff524bd48402921ea28ec695f5a17", "0.2.8--r43hdfd78af_0": "sha256:e9d7a33ed9f5c94f12d93099677b0c1f805ca617cd13a6f91ddfb37f851b2b07", "0.3.0--r43hdfd78af_0": "sha256:d3714ddfac9026d4edc0c17291d136357c7621637108fbe44ba692f4e1f7a3ac", "0.3.0--r44hdfd78af_1": "sha256:63026fff7df18176f26d3c727837cf084632224b99a1c6644d8a90c25bb883f5"}, "docker": "quay.io/biocontainers/r-acidcli"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-acidcli.
shpc-registry automated BioContainers addition for r-acidcli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-acidcli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-acidcli:0.3.0--r44hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-acidcli/0.3.0--r44hdfd78af_1
$ module help quay.io/biocontainers/r-acidcli/0.3.0--r44hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-acidcli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-acidcli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-acidcli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-acidcli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-acidcli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-acidcli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-acidcli

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