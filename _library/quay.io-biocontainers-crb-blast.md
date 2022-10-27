---
layout: container
name:  "quay.io/biocontainers/crb-blast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crb-blast/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/crb-blast/container.yaml"
updated_at: "2022-10-27 00:53:07.356413"
latest: "0.6.6--2"
container_url: "https://biocontainers.pro/tools/crb-blast"
aliases:
 - "bioruby"
 - "br_biofetch.rb"
 - "br_bioflat.rb"
 - "br_biogetseq.rb"
 - "br_pmfetch.rb"
 - "crb-blast"
versions:
 - "0.6.6--2"
description: "shpc-registry automated BioContainers addition for crb-blast"
config: {"url": "https://biocontainers.pro/tools/crb-blast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for crb-blast", "latest": {"0.6.6--2": "sha256:db9c0129f5a0066fc39faf8eac646c29c5fdafad56c35fac7e3bcb7c4a616827"}, "tags": {"0.6.6--2": "sha256:db9c0129f5a0066fc39faf8eac646c29c5fdafad56c35fac7e3bcb7c4a616827"}, "docker": "quay.io/biocontainers/crb-blast", "aliases": {"bioruby": "/usr/local/bin/bioruby", "br_biofetch.rb": "/usr/local/bin/br_biofetch.rb", "br_bioflat.rb": "/usr/local/bin/br_bioflat.rb", "br_biogetseq.rb": "/usr/local/bin/br_biogetseq.rb", "br_pmfetch.rb": "/usr/local/bin/br_pmfetch.rb", "crb-blast": "/usr/local/bin/crb-blast"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crb-blast.
shpc-registry automated BioContainers addition for crb-blast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crb-blast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crb-blast:0.6.6--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crb-blast/0.6.6--2
$ module help quay.io/biocontainers/crb-blast/0.6.6--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crb-blast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crb-blast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crb-blast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crb-blast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crb-blast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crb-blast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bioruby

```bash
$ singularity exec <container> /usr/local/bin/bioruby
$ podman run --it --rm --entrypoint /usr/local/bin/bioruby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioruby   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### br_biofetch.rb

```bash
$ singularity exec <container> /usr/local/bin/br_biofetch.rb
$ podman run --it --rm --entrypoint /usr/local/bin/br_biofetch.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/br_biofetch.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### br_bioflat.rb

```bash
$ singularity exec <container> /usr/local/bin/br_bioflat.rb
$ podman run --it --rm --entrypoint /usr/local/bin/br_bioflat.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/br_bioflat.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### br_biogetseq.rb

```bash
$ singularity exec <container> /usr/local/bin/br_biogetseq.rb
$ podman run --it --rm --entrypoint /usr/local/bin/br_biogetseq.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/br_biogetseq.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### br_pmfetch.rb

```bash
$ singularity exec <container> /usr/local/bin/br_pmfetch.rb
$ podman run --it --rm --entrypoint /usr/local/bin/br_pmfetch.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/br_pmfetch.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crb-blast

```bash
$ singularity exec <container> /usr/local/bin/crb-blast
$ podman run --it --rm --entrypoint /usr/local/bin/crb-blast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crb-blast   -v ${PWD} -w ${PWD} <container> -c " $@"
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