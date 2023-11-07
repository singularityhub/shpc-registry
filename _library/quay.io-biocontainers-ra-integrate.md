---
layout: container
name:  "quay.io/biocontainers/ra-integrate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ra-integrate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ra-integrate/container.yaml"
updated_at: "2023-11-07 03:13:24.235143"
latest: "0.1--0"
container_url: "https://biocontainers.pro/tools/ra-integrate"
aliases:
 - "consensus"
 - "depot"
 - "dotty"
 - "fill_read_coverage"
 - "filter_contained"
 - "filter_erroneous_overlaps"
 - "filter_transitive"
 - "lneato"
 - "overlap2dot"
 - "ra-integrate"
 - "ra_consensus"
 - "to_afg"
 - "unitigger"
 - "widen_overlaps"
 - "zoom"
 - "erb"
 - "gem"
 - "irb"
 - "rake"
 - "rdoc"
 - "ri"
 - "ruby"
 - "easy_install-3.5"
 - "pngcp"
 - "2to3-3.5"
versions:
 - "0.1--0"
description: "shpc-registry automated BioContainers addition for ra-integrate"
config: {"url": "https://biocontainers.pro/tools/ra-integrate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ra-integrate", "latest": {"0.1--0": "sha256:578261c1b4d3f29e249be2e862998606eb8d75eaf0b68eb7b79ae9f77b7af447"}, "tags": {"0.1--0": "sha256:578261c1b4d3f29e249be2e862998606eb8d75eaf0b68eb7b79ae9f77b7af447"}, "docker": "quay.io/biocontainers/ra-integrate", "aliases": {"consensus": "/usr/local/bin/consensus", "depot": "/usr/local/bin/depot", "dotty": "/usr/local/bin/dotty", "fill_read_coverage": "/usr/local/bin/fill_read_coverage", "filter_contained": "/usr/local/bin/filter_contained", "filter_erroneous_overlaps": "/usr/local/bin/filter_erroneous_overlaps", "filter_transitive": "/usr/local/bin/filter_transitive", "lneato": "/usr/local/bin/lneato", "overlap2dot": "/usr/local/bin/overlap2dot", "ra-integrate": "/usr/local/bin/ra-integrate", "ra_consensus": "/usr/local/bin/ra_consensus", "to_afg": "/usr/local/bin/to_afg", "unitigger": "/usr/local/bin/unitigger", "widen_overlaps": "/usr/local/bin/widen_overlaps", "zoom": "/usr/local/bin/zoom", "erb": "/usr/local/bin/erb", "gem": "/usr/local/bin/gem", "irb": "/usr/local/bin/irb", "rake": "/usr/local/bin/rake", "rdoc": "/usr/local/bin/rdoc", "ri": "/usr/local/bin/ri", "ruby": "/usr/local/bin/ruby", "easy_install-3.5": "/usr/local/bin/easy_install-3.5", "pngcp": "/usr/local/bin/pngcp", "2to3-3.5": "/usr/local/bin/2to3-3.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ra-integrate.
shpc-registry automated BioContainers addition for ra-integrate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ra-integrate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ra-integrate:0.1--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ra-integrate/0.1--0
$ module help quay.io/biocontainers/ra-integrate/0.1--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ra-integrate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ra-integrate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ra-integrate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ra-integrate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ra-integrate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ra-integrate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### consensus

```bash
$ singularity exec <container> /usr/local/bin/consensus
$ podman run --it --rm --entrypoint /usr/local/bin/consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### depot

```bash
$ singularity exec <container> /usr/local/bin/depot
$ podman run --it --rm --entrypoint /usr/local/bin/depot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/depot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotty

```bash
$ singularity exec <container> /usr/local/bin/dotty
$ podman run --it --rm --entrypoint /usr/local/bin/dotty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill_read_coverage

```bash
$ singularity exec <container> /usr/local/bin/fill_read_coverage
$ podman run --it --rm --entrypoint /usr/local/bin/fill_read_coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill_read_coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_contained

```bash
$ singularity exec <container> /usr/local/bin/filter_contained
$ podman run --it --rm --entrypoint /usr/local/bin/filter_contained   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_contained   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_erroneous_overlaps

```bash
$ singularity exec <container> /usr/local/bin/filter_erroneous_overlaps
$ podman run --it --rm --entrypoint /usr/local/bin/filter_erroneous_overlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_erroneous_overlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_transitive

```bash
$ singularity exec <container> /usr/local/bin/filter_transitive
$ podman run --it --rm --entrypoint /usr/local/bin/filter_transitive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_transitive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lneato

```bash
$ singularity exec <container> /usr/local/bin/lneato
$ podman run --it --rm --entrypoint /usr/local/bin/lneato   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lneato   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### overlap2dot

```bash
$ singularity exec <container> /usr/local/bin/overlap2dot
$ podman run --it --rm --entrypoint /usr/local/bin/overlap2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/overlap2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ra-integrate

```bash
$ singularity exec <container> /usr/local/bin/ra-integrate
$ podman run --it --rm --entrypoint /usr/local/bin/ra-integrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ra-integrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ra_consensus

```bash
$ singularity exec <container> /usr/local/bin/ra_consensus
$ podman run --it --rm --entrypoint /usr/local/bin/ra_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ra_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### to_afg

```bash
$ singularity exec <container> /usr/local/bin/to_afg
$ podman run --it --rm --entrypoint /usr/local/bin/to_afg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/to_afg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unitigger

```bash
$ singularity exec <container> /usr/local/bin/unitigger
$ podman run --it --rm --entrypoint /usr/local/bin/unitigger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unitigger   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### widen_overlaps

```bash
$ singularity exec <container> /usr/local/bin/widen_overlaps
$ podman run --it --rm --entrypoint /usr/local/bin/widen_overlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/widen_overlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zoom

```bash
$ singularity exec <container> /usr/local/bin/zoom
$ podman run --it --rm --entrypoint /usr/local/bin/zoom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zoom   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### easy_install-3.5

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pngcp

```bash
$ singularity exec <container> /usr/local/bin/pngcp
$ podman run --it --rm --entrypoint /usr/local/bin/pngcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pngcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.5

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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