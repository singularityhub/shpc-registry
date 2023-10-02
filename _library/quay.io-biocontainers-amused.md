---
layout: container
name:  "quay.io/biocontainers/amused"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/amused/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/amused/container.yaml"
updated_at: "2023-10-02 02:47:08.232465"
latest: "1.0--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/amused"
aliases:
 - "AMUSED"
 - "AMUSED-KS"
 - "alignKMers"
 - "bundle"
 - "bundler"
 - "racc"
 - "racc2y"
 - "shuffleCodons.rb"
 - "shuffleCodonsAddMotifs.rb"
 - "y2racc"
 - "gdbm_dump"
 - "gdbm_load"
 - "gdbmtool"
 - "jemalloc-config"
 - "jeprof"
 - "jemalloc.sh"
 - "erb"
 - "gem"
 - "irb"
 - "rake"
versions:
 - "1.0--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for amused"
config: {"url": "https://biocontainers.pro/tools/amused", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for amused", "latest": {"1.0--hdfd78af_3": "sha256:f187cfd645c3544e245f106e9e7234750da644af5abd1e2fff034b6ad379ffa5"}, "tags": {"1.0--hdfd78af_3": "sha256:f187cfd645c3544e245f106e9e7234750da644af5abd1e2fff034b6ad379ffa5"}, "docker": "quay.io/biocontainers/amused", "aliases": {"AMUSED": "/usr/local/bin/AMUSED", "AMUSED-KS": "/usr/local/bin/AMUSED-KS", "alignKMers": "/usr/local/bin/alignKMers", "bundle": "/usr/local/bin/bundle", "bundler": "/usr/local/bin/bundler", "racc": "/usr/local/bin/racc", "racc2y": "/usr/local/bin/racc2y", "shuffleCodons.rb": "/usr/local/bin/shuffleCodons.rb", "shuffleCodonsAddMotifs.rb": "/usr/local/bin/shuffleCodonsAddMotifs.rb", "y2racc": "/usr/local/bin/y2racc", "gdbm_dump": "/usr/local/bin/gdbm_dump", "gdbm_load": "/usr/local/bin/gdbm_load", "gdbmtool": "/usr/local/bin/gdbmtool", "jemalloc-config": "/usr/local/bin/jemalloc-config", "jeprof": "/usr/local/bin/jeprof", "jemalloc.sh": "/usr/local/bin/jemalloc.sh", "erb": "/usr/local/bin/erb", "gem": "/usr/local/bin/gem", "irb": "/usr/local/bin/irb", "rake": "/usr/local/bin/rake"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/amused.
shpc-registry automated BioContainers addition for amused
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/amused
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/amused:1.0--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/amused/1.0--hdfd78af_3
$ module help quay.io/biocontainers/amused/1.0--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### amused-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### amused-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### amused-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### amused-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### amused-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### amused-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AMUSED

```bash
$ singularity exec <container> /usr/local/bin/AMUSED
$ podman run --it --rm --entrypoint /usr/local/bin/AMUSED   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AMUSED   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AMUSED-KS

```bash
$ singularity exec <container> /usr/local/bin/AMUSED-KS
$ podman run --it --rm --entrypoint /usr/local/bin/AMUSED-KS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AMUSED-KS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alignKMers

```bash
$ singularity exec <container> /usr/local/bin/alignKMers
$ podman run --it --rm --entrypoint /usr/local/bin/alignKMers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alignKMers   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### racc

```bash
$ singularity exec <container> /usr/local/bin/racc
$ podman run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racc2y

```bash
$ singularity exec <container> /usr/local/bin/racc2y
$ podman run --it --rm --entrypoint /usr/local/bin/racc2y   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racc2y   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shuffleCodons.rb

```bash
$ singularity exec <container> /usr/local/bin/shuffleCodons.rb
$ podman run --it --rm --entrypoint /usr/local/bin/shuffleCodons.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shuffleCodons.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shuffleCodonsAddMotifs.rb

```bash
$ singularity exec <container> /usr/local/bin/shuffleCodonsAddMotifs.rb
$ podman run --it --rm --entrypoint /usr/local/bin/shuffleCodonsAddMotifs.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shuffleCodonsAddMotifs.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### y2racc

```bash
$ singularity exec <container> /usr/local/bin/y2racc
$ podman run --it --rm --entrypoint /usr/local/bin/y2racc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/y2racc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jemalloc-config

```bash
$ singularity exec <container> /usr/local/bin/jemalloc-config
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jeprof

```bash
$ singularity exec <container> /usr/local/bin/jeprof
$ podman run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc.sh

```bash
$ singularity exec <container> /usr/local/bin/jemalloc.sh
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### erb

```bash
$ singularity exec <container> /usr/local/bin/erb
$ podman run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem

```bash
$ singularity exec <container> /usr/local/bin/gem
$ podman run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irb

```bash
$ singularity exec <container> /usr/local/bin/irb
$ podman run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rake

```bash
$ singularity exec <container> /usr/local/bin/rake
$ podman run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
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