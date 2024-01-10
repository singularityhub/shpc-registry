---
layout: container
name:  "quay.io/biocontainers/newick_utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/newick_utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/newick_utils/container.yaml"
updated_at: "2024-01-10 02:32:42.923119"
latest: "1.6--h031d066_7"
container_url: "https://biocontainers.pro/tools/newick_utils"
aliases:
 - "nw_clade"
 - "nw_condense"
 - "nw_display"
 - "nw_distance"
 - "nw_duration"
 - "nw_ed"
 - "nw_gen"
 - "nw_indent"
 - "nw_labels"
 - "nw_match"
 - "nw_order"
 - "nw_prune"
 - "nw_rename"
 - "nw_reroot"
 - "nw_stats"
 - "nw_support"
 - "nw_topology"
 - "nw_trim"
versions:
 - "1.6--hec16e2b_5"
 - "1.6--h031d066_7"
description: "shpc-registry automated BioContainers addition for newick_utils"
config: {"url": "https://biocontainers.pro/tools/newick_utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for newick_utils", "latest": {"1.6--h031d066_7": "sha256:14b7b2cc7069cfc8d9ab0dfba0964e5fb5ac4eecbb1aa518c98b12c824c3b410"}, "tags": {"1.6--hec16e2b_5": "sha256:9bc5359a806cb9d07e0c41d5a9445321c2765a309b6564a0d5482307420c8d76", "1.6--h031d066_7": "sha256:14b7b2cc7069cfc8d9ab0dfba0964e5fb5ac4eecbb1aa518c98b12c824c3b410"}, "docker": "quay.io/biocontainers/newick_utils", "aliases": {"nw_clade": "/usr/local/bin/nw_clade", "nw_condense": "/usr/local/bin/nw_condense", "nw_display": "/usr/local/bin/nw_display", "nw_distance": "/usr/local/bin/nw_distance", "nw_duration": "/usr/local/bin/nw_duration", "nw_ed": "/usr/local/bin/nw_ed", "nw_gen": "/usr/local/bin/nw_gen", "nw_indent": "/usr/local/bin/nw_indent", "nw_labels": "/usr/local/bin/nw_labels", "nw_match": "/usr/local/bin/nw_match", "nw_order": "/usr/local/bin/nw_order", "nw_prune": "/usr/local/bin/nw_prune", "nw_rename": "/usr/local/bin/nw_rename", "nw_reroot": "/usr/local/bin/nw_reroot", "nw_stats": "/usr/local/bin/nw_stats", "nw_support": "/usr/local/bin/nw_support", "nw_topology": "/usr/local/bin/nw_topology", "nw_trim": "/usr/local/bin/nw_trim"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/newick_utils.
shpc-registry automated BioContainers addition for newick_utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/newick_utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/newick_utils:1.6--h031d066_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/newick_utils/1.6--h031d066_7
$ module help quay.io/biocontainers/newick_utils/1.6--h031d066_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### newick_utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### newick_utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### newick_utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### newick_utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### newick_utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### newick_utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nw_clade

```bash
$ singularity exec <container> /usr/local/bin/nw_clade
$ podman run --it --rm --entrypoint /usr/local/bin/nw_clade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_clade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_condense

```bash
$ singularity exec <container> /usr/local/bin/nw_condense
$ podman run --it --rm --entrypoint /usr/local/bin/nw_condense   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_condense   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_display

```bash
$ singularity exec <container> /usr/local/bin/nw_display
$ podman run --it --rm --entrypoint /usr/local/bin/nw_display   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_display   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_distance

```bash
$ singularity exec <container> /usr/local/bin/nw_distance
$ podman run --it --rm --entrypoint /usr/local/bin/nw_distance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_distance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_duration

```bash
$ singularity exec <container> /usr/local/bin/nw_duration
$ podman run --it --rm --entrypoint /usr/local/bin/nw_duration   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_duration   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_ed

```bash
$ singularity exec <container> /usr/local/bin/nw_ed
$ podman run --it --rm --entrypoint /usr/local/bin/nw_ed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_ed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_gen

```bash
$ singularity exec <container> /usr/local/bin/nw_gen
$ podman run --it --rm --entrypoint /usr/local/bin/nw_gen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_gen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_indent

```bash
$ singularity exec <container> /usr/local/bin/nw_indent
$ podman run --it --rm --entrypoint /usr/local/bin/nw_indent   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_indent   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_labels

```bash
$ singularity exec <container> /usr/local/bin/nw_labels
$ podman run --it --rm --entrypoint /usr/local/bin/nw_labels   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_labels   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_match

```bash
$ singularity exec <container> /usr/local/bin/nw_match
$ podman run --it --rm --entrypoint /usr/local/bin/nw_match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_order

```bash
$ singularity exec <container> /usr/local/bin/nw_order
$ podman run --it --rm --entrypoint /usr/local/bin/nw_order   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_order   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_prune

```bash
$ singularity exec <container> /usr/local/bin/nw_prune
$ podman run --it --rm --entrypoint /usr/local/bin/nw_prune   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_prune   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_rename

```bash
$ singularity exec <container> /usr/local/bin/nw_rename
$ podman run --it --rm --entrypoint /usr/local/bin/nw_rename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_rename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_reroot

```bash
$ singularity exec <container> /usr/local/bin/nw_reroot
$ podman run --it --rm --entrypoint /usr/local/bin/nw_reroot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_reroot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_stats

```bash
$ singularity exec <container> /usr/local/bin/nw_stats
$ podman run --it --rm --entrypoint /usr/local/bin/nw_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_support

```bash
$ singularity exec <container> /usr/local/bin/nw_support
$ podman run --it --rm --entrypoint /usr/local/bin/nw_support   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_support   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_topology

```bash
$ singularity exec <container> /usr/local/bin/nw_topology
$ podman run --it --rm --entrypoint /usr/local/bin/nw_topology   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_topology   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_trim

```bash
$ singularity exec <container> /usr/local/bin/nw_trim
$ podman run --it --rm --entrypoint /usr/local/bin/nw_trim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_trim   -v ${PWD} -w ${PWD} <container> -c " $@"
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