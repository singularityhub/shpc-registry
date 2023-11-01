---
layout: container
name:  "quay.io/biocontainers/annonars"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/annonars/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/annonars/container.yaml"
updated_at: "2023-11-01 02:44:36.550787"
latest: "0.24.2--hb3cd794_0"
container_url: "https://biocontainers.pro/tools/annonars"
aliases:
 - "annonars"
versions:
 - "0.5.0--h63738d7_0"
 - "0.12.7--hb3cd794_0"
 - "0.10.0--hb3cd794_0"
 - "0.9.0--hb3cd794_0"
 - "0.8.0--hb3cd794_0"
 - "0.7.0--h63738d7_0"
 - "0.12.9--hb3cd794_0"
 - "0.14.1--hb3cd794_0"
 - "0.13.0--hb3cd794_0"
 - "0.20.0--hb3cd794_0"
 - "0.19.0--hb3cd794_0"
 - "0.18.0--hb3cd794_0"
 - "0.17.0--hb3cd794_0"
 - "0.16.0--hb3cd794_0"
 - "0.24.2--hb3cd794_0"
 - "0.23.1--hb3cd794_0"
 - "0.22.0--hb3cd794_0"
 - "0.21.1--hb3cd794_0"
description: "singularity registry hpc automated addition for annonars"
config: {"url": "https://biocontainers.pro/tools/annonars", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for annonars", "latest": {"0.24.2--hb3cd794_0": "sha256:041354176b1f3117d47029716bd282d9461b7cdf6b60a399b8771498fc927a1c"}, "tags": {"0.5.0--h63738d7_0": "sha256:5c330116a257365c8c35ef82850d493137dd6c0dd3fbb2d113eabf356409491e", "0.12.7--hb3cd794_0": "sha256:7068702067a6837695fd8da00383ada8a70db205fc69e75d7735d71889e73ecd", "0.10.0--hb3cd794_0": "sha256:3fad81a9c0d13512a8917cb48b84e273b1e8eb6e8a7cd6a7599463c4d5109acd", "0.9.0--hb3cd794_0": "sha256:de91626222e5568b8d998a8b24b78b4ab78edac4077e50dcb66824a7374aec93", "0.8.0--hb3cd794_0": "sha256:a6a345fe351fecaed0fb2372ecafebb0c8fc804a2f3b16b69a6faa28338d2eee", "0.7.0--h63738d7_0": "sha256:de35b06de23d6f4df74c2e3a1b42febf3d2476f5810846b140958ba90b4201dd", "0.12.9--hb3cd794_0": "sha256:b0a420a65017e46019997c5bc3557cb454f378cf958174029e565c6d292170ab", "0.14.1--hb3cd794_0": "sha256:61e962766c9f0bcba72a98ca97443421b9c9da2e38102f448bd912f7c5ca67e2", "0.13.0--hb3cd794_0": "sha256:c064deee445c6bddaecf2f0c6e113977ea2d4be54d1e1301bc2131078451c3cf", "0.20.0--hb3cd794_0": "sha256:c57aa2f6e7c49bdadf44e1b540993ff511312a3af5a47ca6bf3059c032f34319", "0.19.0--hb3cd794_0": "sha256:fdfa8a7af43b95568a23039ce129feed601620a9c92d104c8305ac40a5de452b", "0.18.0--hb3cd794_0": "sha256:dc3af0fd10d09b1e5cbbcba293440657c09672800109ee92459eacfe4e33594e", "0.17.0--hb3cd794_0": "sha256:6033539b20dc077a413d8b0e27ed22817023f8e395d7e7b95afab71b6372ebc1", "0.16.0--hb3cd794_0": "sha256:37d2e717e8788599ecd6c620cec4136faf6237c5221be3347702159f7cbdc4db", "0.24.2--hb3cd794_0": "sha256:041354176b1f3117d47029716bd282d9461b7cdf6b60a399b8771498fc927a1c", "0.23.1--hb3cd794_0": "sha256:8d3a1daa52f3cea7357c4a83c8206164d13913da775840e0cb0416756ab3c50c", "0.22.0--hb3cd794_0": "sha256:8b6f735ae9ae824a9c0e6ae3542eb89eed57484083c1f040cac7880339c89d86", "0.21.1--hb3cd794_0": "sha256:0c17e9e4acaceac95227da7a427bbca86a2e54d024bd2d58bb0725c2107224b8"}, "docker": "quay.io/biocontainers/annonars", "aliases": {"annonars": "/usr/local/bin/annonars"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/annonars.
singularity registry hpc automated addition for annonars
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/annonars
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/annonars:0.24.2--hb3cd794_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/annonars/0.24.2--hb3cd794_0
$ module help quay.io/biocontainers/annonars/0.24.2--hb3cd794_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### annonars-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### annonars-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### annonars-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### annonars-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### annonars-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### annonars-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annonars

```bash
$ singularity exec <container> /usr/local/bin/annonars
$ podman run --it --rm --entrypoint /usr/local/bin/annonars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annonars   -v ${PWD} -w ${PWD} <container> -c " $@"
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