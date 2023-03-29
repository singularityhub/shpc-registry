---
layout: container
name:  "quay.io/biocontainers/ragtag"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ragtag/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ragtag/container.yaml"
updated_at: "2023-03-29 02:44:33.319434"
latest: "2.1.0--pyhb7b1952_0"
container_url: "https://biocontainers.pro/tools/ragtag"
aliases:
 - "ragtag.py"
 - "ragtag_agp2fa.py"
 - "ragtag_agpcheck.py"
 - "ragtag_asmstats.py"
 - "ragtag_break_query.py"
 - "ragtag_correct.py"
 - "ragtag_create_links.py"
 - "ragtag_delta2paf.py"
 - "ragtag_merge.py"
 - "ragtag_paf2delta.py"
 - "ragtag_patch.py"
 - "ragtag_rename.py"
 - "ragtag_scaffold.py"
 - "ragtag_splitasm.py"
 - "ragtag_stats.py"
 - "ragtag_update_gff.py"
 - "setup.py"
 - "mapview"
 - "mgaps"
 - "run-mummer1"
 - "run-mummer3"
 - "combineMUMs"
 - "delta-filter"
 - "dnadiff"
 - "exact-tandems"
 - "mummer"
 - "mummerplot"
versions:
 - "2.1.0--pyhb7b1952_0"
description: "shpc-registry automated BioContainers addition for ragtag"
config: {"url": "https://biocontainers.pro/tools/ragtag", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ragtag", "latest": {"2.1.0--pyhb7b1952_0": "sha256:88e12e008e8301df8b3797b4bfff551534accf92f194daae65dbb3ed78da1580"}, "tags": {"2.1.0--pyhb7b1952_0": "sha256:88e12e008e8301df8b3797b4bfff551534accf92f194daae65dbb3ed78da1580"}, "docker": "quay.io/biocontainers/ragtag", "aliases": {"ragtag.py": "/usr/local/bin/ragtag.py", "ragtag_agp2fa.py": "/usr/local/bin/ragtag_agp2fa.py", "ragtag_agpcheck.py": "/usr/local/bin/ragtag_agpcheck.py", "ragtag_asmstats.py": "/usr/local/bin/ragtag_asmstats.py", "ragtag_break_query.py": "/usr/local/bin/ragtag_break_query.py", "ragtag_correct.py": "/usr/local/bin/ragtag_correct.py", "ragtag_create_links.py": "/usr/local/bin/ragtag_create_links.py", "ragtag_delta2paf.py": "/usr/local/bin/ragtag_delta2paf.py", "ragtag_merge.py": "/usr/local/bin/ragtag_merge.py", "ragtag_paf2delta.py": "/usr/local/bin/ragtag_paf2delta.py", "ragtag_patch.py": "/usr/local/bin/ragtag_patch.py", "ragtag_rename.py": "/usr/local/bin/ragtag_rename.py", "ragtag_scaffold.py": "/usr/local/bin/ragtag_scaffold.py", "ragtag_splitasm.py": "/usr/local/bin/ragtag_splitasm.py", "ragtag_stats.py": "/usr/local/bin/ragtag_stats.py", "ragtag_update_gff.py": "/usr/local/bin/ragtag_update_gff.py", "setup.py": "/usr/local/bin/setup.py", "mapview": "/usr/local/bin/mapview", "mgaps": "/usr/local/bin/mgaps", "run-mummer1": "/usr/local/bin/run-mummer1", "run-mummer3": "/usr/local/bin/run-mummer3", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems", "mummer": "/usr/local/bin/mummer", "mummerplot": "/usr/local/bin/mummerplot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ragtag.
shpc-registry automated BioContainers addition for ragtag
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ragtag
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ragtag:2.1.0--pyhb7b1952_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ragtag/2.1.0--pyhb7b1952_0
$ module help quay.io/biocontainers/ragtag/2.1.0--pyhb7b1952_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ragtag-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ragtag-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ragtag-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ragtag-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ragtag-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ragtag-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ragtag.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_agp2fa.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_agp2fa.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_agp2fa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_agp2fa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_agpcheck.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_agpcheck.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_agpcheck.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_agpcheck.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_asmstats.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_asmstats.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_asmstats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_asmstats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_break_query.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_break_query.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_break_query.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_break_query.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_correct.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_correct.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_correct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_correct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_create_links.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_create_links.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_create_links.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_create_links.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_delta2paf.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_delta2paf.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_delta2paf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_delta2paf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_merge.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_paf2delta.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_paf2delta.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_paf2delta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_paf2delta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_patch.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_patch.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_patch.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_patch.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_rename.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_rename.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_rename.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_rename.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_scaffold.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_scaffold.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_scaffold.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_scaffold.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_splitasm.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_splitasm.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_splitasm.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_splitasm.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_stats.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_stats.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_stats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_stats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ragtag_update_gff.py

```bash
$ singularity exec <container> /usr/local/bin/ragtag_update_gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/ragtag_update_gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ragtag_update_gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup.py

```bash
$ singularity exec <container> /usr/local/bin/setup.py
$ podman run --it --rm --entrypoint /usr/local/bin/setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapview

```bash
$ singularity exec <container> /usr/local/bin/mapview
$ podman run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mgaps

```bash
$ singularity exec <container> /usr/local/bin/mgaps
$ podman run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer1

```bash
$ singularity exec <container> /usr/local/bin/run-mummer1
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer3

```bash
$ singularity exec <container> /usr/local/bin/run-mummer3
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMUMs

```bash
$ singularity exec <container> /usr/local/bin/combineMUMs
$ podman run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta-filter

```bash
$ singularity exec <container> /usr/local/bin/delta-filter
$ podman run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadiff

```bash
$ singularity exec <container> /usr/local/bin/dnadiff
$ podman run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exact-tandems

```bash
$ singularity exec <container> /usr/local/bin/exact-tandems
$ podman run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummer

```bash
$ singularity exec <container> /usr/local/bin/mummer
$ podman run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummerplot

```bash
$ singularity exec <container> /usr/local/bin/mummerplot
$ podman run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
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