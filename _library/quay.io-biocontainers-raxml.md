---
layout: container
name:  "quay.io/biocontainers/raxml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/raxml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/raxml/container.yaml"
updated_at: "2023-12-29 02:38:51.842496"
latest: "8.2.13--h031d066_0"
container_url: "https://biocontainers.pro/tools/raxml"

versions:
 - "8.2.9--hec16e2b_5"
 - "8.2.12--hec16e2b_4"
 - "8.2.12--hec16e2b_5"
 - "8.2.12--h031d066_6"
 - "8.2.13--h031d066_0"
description: "shpc-registry automated BioContainers addition for raxml"
config: {"url": "https://biocontainers.pro/tools/raxml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for raxml", "latest": {"8.2.13--h031d066_0": "sha256:ae1ae1335c6bb25c2715fc280e0ba08822ac5f208c59fbd5e07b546135e905d8"}, "tags": {"8.2.9--hec16e2b_5": "sha256:f563217a34a3ae2f4766aa4650851ea91ac0178a906a66dc31223ed7f055518c", "8.2.12--hec16e2b_4": "sha256:30407bd43203e64dfc0f4bd15778b11f75f53101caaa369042c66c457f9bb8a6", "8.2.12--hec16e2b_5": "sha256:bedffbd2dd608c568ad1acbc1a9b2553c5b7c996ccf640fa164237cbdfe34698", "8.2.12--h031d066_6": "sha256:3489e0f63ec040e5ceb1a78f5137eb4c200d015bac5ff3c677d23b031a89f81a", "8.2.13--h031d066_0": "sha256:ae1ae1335c6bb25c2715fc280e0ba08822ac5f208c59fbd5e07b546135e905d8"}, "docker": "quay.io/biocontainers/raxml"}
---

This module is a singularity container wrapper for quay.io/biocontainers/raxml.
shpc-registry automated BioContainers addition for raxml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/raxml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/raxml:8.2.13--h031d066_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/raxml/8.2.13--h031d066_0
$ module help quay.io/biocontainers/raxml/8.2.13--h031d066_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### raxml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### raxml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### raxml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### raxml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### raxml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### raxml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### raxml

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