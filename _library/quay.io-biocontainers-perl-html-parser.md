---
layout: container
name:  "quay.io/biocontainers/perl-html-parser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-html-parser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-html-parser/container.yaml"
updated_at: "2025-10-18 03:44:53.741412"
latest: "3.83--pl5321h9948957_1"
container_url: "https://biocontainers.pro/tools/perl-html-parser"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "3.79--pl5321h9f5acd7_0"
 - "3.80--pl5321h9f5acd7_0"
 - "3.81--pl5321h9f5acd7_0"
 - "3.81--pl5321h4ac6f70_1"
 - "3.81--pl5321h9948957_2"
 - "3.83--pl5321h9948957_0"
 - "3.81--pl5321h9948957_3"
 - "3.83--pl5321h9948957_1"
description: "shpc-registry automated BioContainers addition for perl-html-parser"
config: {"url": "https://biocontainers.pro/tools/perl-html-parser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-html-parser", "latest": {"3.83--pl5321h9948957_1": "sha256:75085df299851461bc296b17b7e2361d138ca98e6f40b031bdface066bd3b0e2"}, "tags": {"3.79--pl5321h9f5acd7_0": "sha256:5b1b36262cfba67cb7aedac234e2eac0dc53abf720baebc320ad07a1e6edd985", "3.80--pl5321h9f5acd7_0": "sha256:eb501abf500be9d4982bd1afda9525bfb3a1a7b9fc67fab4d38e829458146f05", "3.81--pl5321h9f5acd7_0": "sha256:c0f17dfa1034030d75033258170c5bede1ff064af89e4f260c4bb6bb3976177f", "3.81--pl5321h4ac6f70_1": "sha256:0c432db90f26c8bb192445a2ab13783a927d29c1d7fa86e7a0e866c1c9a04a7a", "3.81--pl5321h9948957_2": "sha256:c5e2e6872d841452b2c2e0bebce2a1ad6126cc722de9e27ede4f2f1d7fde57e3", "3.83--pl5321h9948957_0": "sha256:912115e952ed94b9a35b868451a9c3d89ee098107041617ecdf8c982564256e2", "3.81--pl5321h9948957_3": "sha256:475b31abbad17236331cc8eb9957388f0380585eaf6f6cfeeee5c142452c2caf", "3.83--pl5321h9948957_1": "sha256:75085df299851461bc296b17b7e2361d138ca98e6f40b031bdface066bd3b0e2"}, "docker": "quay.io/biocontainers/perl-html-parser", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-html-parser.
shpc-registry automated BioContainers addition for perl-html-parser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-html-parser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-html-parser:3.83--pl5321h9948957_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-html-parser/3.83--pl5321h9948957_1
$ module help quay.io/biocontainers/perl-html-parser/3.83--pl5321h9948957_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-html-parser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-html-parser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-html-parser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-html-parser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-html-parser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-html-parser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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