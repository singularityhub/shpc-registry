---
layout: container
name:  "quay.io/biocontainers/crb-blast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crb-blast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/crb-blast/container.yaml"
updated_at: "2024-10-16 03:18:48.792236"
latest: "0.6.9--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/crb-blast"
aliases:
 - "bioruby"
 - "br_biofetch.rb"
 - "br_bioflat.rb"
 - "br_biogetseq.rb"
 - "br_pmfetch.rb"
 - "bundle"
 - "bundler"
 - "crb-blast"
 - "gdbm_dump"
 - "gdbm_load"
 - "gdbmtool"
 - "build.sh"
 - "common.go"
 - "rchive.go"
 - "setup-deps.log"
 - "setup.sh"
 - "xtract.go"
 - "erb"
versions:
 - "0.6.6--2"
 - "0.6.9--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for crb-blast"
config: {"url": "https://biocontainers.pro/tools/crb-blast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for crb-blast", "latest": {"0.6.9--hdfd78af_0": "sha256:8398d7ad34176c13e93fc852354f6da91fa30aad2faa029729b428b8f62e6a33"}, "tags": {"0.6.6--2": "sha256:51a165d99e4ba6cec2179137711ac253f4a3409381e24aab1a6b26bbc68563e9", "0.6.9--hdfd78af_0": "sha256:8398d7ad34176c13e93fc852354f6da91fa30aad2faa029729b428b8f62e6a33"}, "docker": "quay.io/biocontainers/crb-blast", "aliases": {"bioruby": "/usr/local/bin/bioruby", "br_biofetch.rb": "/usr/local/bin/br_biofetch.rb", "br_bioflat.rb": "/usr/local/bin/br_bioflat.rb", "br_biogetseq.rb": "/usr/local/bin/br_biogetseq.rb", "br_pmfetch.rb": "/usr/local/bin/br_pmfetch.rb", "bundle": "/usr/local/bin/bundle", "bundler": "/usr/local/bin/bundler", "crb-blast": "/usr/local/bin/crb-blast", "gdbm_dump": "/usr/local/bin/gdbm_dump", "gdbm_load": "/usr/local/bin/gdbm_load", "gdbmtool": "/usr/local/bin/gdbmtool", "build.sh": "/usr/local/bin/build.sh", "common.go": "/usr/local/bin/common.go", "rchive.go": "/usr/local/bin/rchive.go", "setup-deps.log": "/usr/local/bin/setup-deps.log", "setup.sh": "/usr/local/bin/setup.sh", "xtract.go": "/usr/local/bin/xtract.go", "erb": "/usr/local/bin/erb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crb-blast.
shpc-registry automated BioContainers addition for crb-blast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crb-blast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crb-blast:0.6.9--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crb-blast/0.6.9--hdfd78af_0
$ module help quay.io/biocontainers/crb-blast/0.6.9--hdfd78af_0
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


#### bundle

```bash
$ singularity exec <container> /usr/local/bin/bundle
$ podman run --it --rm --entrypoint /usr/local/bin/bundle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundler

```bash
$ singularity exec <container> /usr/local/bin/bundler
$ podman run --it --rm --entrypoint /usr/local/bin/bundler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crb-blast

```bash
$ singularity exec <container> /usr/local/bin/crb-blast
$ podman run --it --rm --entrypoint /usr/local/bin/crb-blast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crb-blast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbm_dump

```bash
$ singularity exec <container> /usr/local/bin/gdbm_dump
$ podman run --it --rm --entrypoint /usr/local/bin/gdbm_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbm_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbm_load

```bash
$ singularity exec <container> /usr/local/bin/gdbm_load
$ podman run --it --rm --entrypoint /usr/local/bin/gdbm_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbm_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbmtool

```bash
$ singularity exec <container> /usr/local/bin/gdbmtool
$ podman run --it --rm --entrypoint /usr/local/bin/gdbmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build.sh

```bash
$ singularity exec <container> /usr/local/bin/build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### common.go

```bash
$ singularity exec <container> /usr/local/bin/common.go
$ podman run --it --rm --entrypoint /usr/local/bin/common.go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/common.go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rchive.go

```bash
$ singularity exec <container> /usr/local/bin/rchive.go
$ podman run --it --rm --entrypoint /usr/local/bin/rchive.go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rchive.go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup-deps.log

```bash
$ singularity exec <container> /usr/local/bin/setup-deps.log
$ podman run --it --rm --entrypoint /usr/local/bin/setup-deps.log   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup-deps.log   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup.sh

```bash
$ singularity exec <container> /usr/local/bin/setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtract.go

```bash
$ singularity exec <container> /usr/local/bin/xtract.go
$ podman run --it --rm --entrypoint /usr/local/bin/xtract.go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtract.go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### erb

```bash
$ singularity exec <container> /usr/local/bin/erb
$ podman run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
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