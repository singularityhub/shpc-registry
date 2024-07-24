---
layout: container
name:  "quay.io/biocontainers/r-acidbase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-acidbase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-acidbase/container.yaml"
updated_at: "2024-07-24 02:41:12.399416"
latest: "0.7.3--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-acidbase"

versions:
 - "0.5.0--r41hdfd78af_0"
 - "0.6.9--r42hdfd78af_0"
 - "0.5.0--r41hdfd78af_1"
 - "0.6.12--r42hdfd78af_0"
 - "0.6.12--r42hdfd78af_1"
 - "0.6.13--r42hdfd78af_0"
 - "0.6.16--r42hdfd78af_0"
 - "0.6.16--r43hdfd78af_1"
 - "0.6.19--r43hdfd78af_0"
 - "0.6.21--r43hdfd78af_0"
 - "0.7.3--r43hdfd78af_1"
 - "0.6.23--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-acidbase"
config: {"url": "https://biocontainers.pro/tools/r-acidbase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-acidbase", "latest": {"0.7.3--r43hdfd78af_1": "sha256:4e9bf919423356a030c41a618e728555ea7f377d99cba90530c3764d4796869e"}, "tags": {"0.5.0--r41hdfd78af_0": "sha256:a871cc05540ff5d001bf95c659f2017e53f04fb03b4ebb056b69ad787f7931cc", "0.6.9--r42hdfd78af_0": "sha256:8bed78a11cef0db40395015c2e902d417f6fed5b07b87406f78c453a2b33ba3f", "0.5.0--r41hdfd78af_1": "sha256:57f49058c0eb7e1784aaa7045a6ebca13ee7c1bdd7e1572d1ce1a70438fba188", "0.6.12--r42hdfd78af_0": "sha256:a1f0a1d80b88a21e96f9312eaa7a1cf3db5e4137ba92eef82d73b14e3bcc5d29", "0.6.12--r42hdfd78af_1": "sha256:4f7a41b606c3ecfb9dbb74c3be5b5d82d131aa7c0421a58e4365251cea234912", "0.6.13--r42hdfd78af_0": "sha256:8bc47efd0d27bb15f26708eb2388e54afa1bae7e38d6429f96b41a1eb87146dc", "0.6.16--r42hdfd78af_0": "sha256:4cf49ffce63e516baa167ab0175c6bbbf5632468009b0966c936ea3b2e8df5d5", "0.6.16--r43hdfd78af_1": "sha256:c1d76607183a20b2e7f05dfd789b0bc7f2c4169dd7acfcdd874fe681849e5425", "0.6.19--r43hdfd78af_0": "sha256:0f97e916d63913dac74e03a7c7d979037ad7602a75aedf6713a50c7f094c3e9c", "0.6.21--r43hdfd78af_0": "sha256:1584c2625714c78c2f86f7115307a6dc1a304c79835249d917715a909362d5d2", "0.7.3--r43hdfd78af_1": "sha256:4e9bf919423356a030c41a618e728555ea7f377d99cba90530c3764d4796869e", "0.6.23--r43hdfd78af_0": "sha256:8731fd1dced867240258db0c8efb57a87853d201b136a1ddf7625ab1515f6737"}, "docker": "quay.io/biocontainers/r-acidbase"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-acidbase.
shpc-registry automated BioContainers addition for r-acidbase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-acidbase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-acidbase:0.7.3--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-acidbase/0.7.3--r43hdfd78af_1
$ module help quay.io/biocontainers/r-acidbase/0.7.3--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-acidbase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-acidbase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-acidbase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-acidbase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-acidbase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-acidbase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-acidbase

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