---
layout: container
name:  "quay.io/biocontainers/renet2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/renet2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/renet2/container.yaml"
updated_at: "2024-08-08 04:20:52.116286"
latest: "1.2--py_0"
container_url: "https://biocontainers.pro/tools/renet2"
aliases:
 - "bundle"
 - "bundler"
 - "racc"
 - "racc2y"
 - "renet2"
 - "y2racc"
 - "gdbm_dump"
 - "gdbm_load"
 - "gdbmtool"
 - "erb"
 - "gem"
 - "irb"
 - "rake"
 - "rdoc"
 - "ri"
 - "ruby"
versions:
 - "1.2--py_0"
description: "shpc-registry automated BioContainers addition for renet2"
config: {"url": "https://biocontainers.pro/tools/renet2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for renet2", "latest": {"1.2--py_0": "sha256:17278bcdf513dfad2523d58233f66ea3cd9b3df7563444aaaf4321c4ca0926c5"}, "tags": {"1.2--py_0": "sha256:17278bcdf513dfad2523d58233f66ea3cd9b3df7563444aaaf4321c4ca0926c5"}, "docker": "quay.io/biocontainers/renet2", "aliases": {"bundle": "/usr/local/bin/bundle", "bundler": "/usr/local/bin/bundler", "racc": "/usr/local/bin/racc", "racc2y": "/usr/local/bin/racc2y", "renet2": "/usr/local/bin/renet2", "y2racc": "/usr/local/bin/y2racc", "gdbm_dump": "/usr/local/bin/gdbm_dump", "gdbm_load": "/usr/local/bin/gdbm_load", "gdbmtool": "/usr/local/bin/gdbmtool", "erb": "/usr/local/bin/erb", "gem": "/usr/local/bin/gem", "irb": "/usr/local/bin/irb", "rake": "/usr/local/bin/rake", "rdoc": "/usr/local/bin/rdoc", "ri": "/usr/local/bin/ri", "ruby": "/usr/local/bin/ruby"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/renet2.
shpc-registry automated BioContainers addition for renet2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/renet2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/renet2:1.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/renet2/1.2--py_0
$ module help quay.io/biocontainers/renet2/1.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### renet2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### renet2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### renet2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### renet2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### renet2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### renet2-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### renet2

```bash
$ singularity exec <container> /usr/local/bin/renet2
$ podman run --it --rm --entrypoint /usr/local/bin/renet2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/renet2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### rdoc

```bash
$ singularity exec <container> /usr/local/bin/rdoc
$ podman run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ri

```bash
$ singularity exec <container> /usr/local/bin/ri
$ podman run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ruby

```bash
$ singularity exec <container> /usr/local/bin/ruby
$ podman run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
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