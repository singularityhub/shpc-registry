---
layout: container
name:  "quay.io/biocontainers/metaphlan2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaphlan2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metaphlan2/container.yaml"
updated_at: "2022-10-27 01:13:49.824615"
latest: "2.96.1--py_0"
container_url: "https://biocontainers.pro/tools/metaphlan2"
aliases:
 - "add_metadata_tree.py"
 - "build_tree_single_strain.py"
 - "compute_distance.py"
 - "compute_distance_all.py"
 - "dump_file.py"
 - "extract_markers.py"
 - "fastx_len_filter.py"
 - "fix_AF1.py"
 - "merge_metaphlan_tables.py"
 - "metaphlan2.py"
 - "metaphlan2krona.py"
 - "mixed_utils.py"
 - "ooSubprocess.py"
 - "plot_bug.py"
 - "plot_tree_ete2.py"
 - "plot_tree_graphlan.py"
 - "read_fastx.py"
 - "sam_filter.py"
 - "sample2markers.py"
 - "strainphlan.py"
 - "which.py"
versions:
 - "2.96.1--py_0"
description: "shpc-registry automated BioContainers addition for metaphlan2"
config: {"url": "https://biocontainers.pro/tools/metaphlan2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaphlan2", "latest": {"2.96.1--py_0": "sha256:950ebbeb2d2c079e77738068b85758b904373c4e3eaf72d511575ef4baaa4924"}, "tags": {"2.96.1--py_0": "sha256:950ebbeb2d2c079e77738068b85758b904373c4e3eaf72d511575ef4baaa4924"}, "docker": "quay.io/biocontainers/metaphlan2", "aliases": {"add_metadata_tree.py": "/usr/local/bin/add_metadata_tree.py", "build_tree_single_strain.py": "/usr/local/bin/build_tree_single_strain.py", "compute_distance.py": "/usr/local/bin/compute_distance.py", "compute_distance_all.py": "/usr/local/bin/compute_distance_all.py", "dump_file.py": "/usr/local/bin/dump_file.py", "extract_markers.py": "/usr/local/bin/extract_markers.py", "fastx_len_filter.py": "/usr/local/bin/fastx_len_filter.py", "fix_AF1.py": "/usr/local/bin/fix_AF1.py", "merge_metaphlan_tables.py": "/usr/local/bin/merge_metaphlan_tables.py", "metaphlan2.py": "/usr/local/bin/metaphlan2.py", "metaphlan2krona.py": "/usr/local/bin/metaphlan2krona.py", "mixed_utils.py": "/usr/local/bin/mixed_utils.py", "ooSubprocess.py": "/usr/local/bin/ooSubprocess.py", "plot_bug.py": "/usr/local/bin/plot_bug.py", "plot_tree_ete2.py": "/usr/local/bin/plot_tree_ete2.py", "plot_tree_graphlan.py": "/usr/local/bin/plot_tree_graphlan.py", "read_fastx.py": "/usr/local/bin/read_fastx.py", "sam_filter.py": "/usr/local/bin/sam_filter.py", "sample2markers.py": "/usr/local/bin/sample2markers.py", "strainphlan.py": "/usr/local/bin/strainphlan.py", "which.py": "/usr/local/bin/which.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaphlan2.
shpc-registry automated BioContainers addition for metaphlan2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaphlan2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaphlan2:2.96.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaphlan2/2.96.1--py_0
$ module help quay.io/biocontainers/metaphlan2/2.96.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaphlan2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaphlan2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaphlan2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaphlan2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaphlan2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaphlan2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_metadata_tree.py

```bash
$ singularity exec <container> /usr/local/bin/add_metadata_tree.py
$ podman run --it --rm --entrypoint /usr/local/bin/add_metadata_tree.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_metadata_tree.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_tree_single_strain.py

```bash
$ singularity exec <container> /usr/local/bin/build_tree_single_strain.py
$ podman run --it --rm --entrypoint /usr/local/bin/build_tree_single_strain.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_tree_single_strain.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compute_distance.py

```bash
$ singularity exec <container> /usr/local/bin/compute_distance.py
$ podman run --it --rm --entrypoint /usr/local/bin/compute_distance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute_distance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compute_distance_all.py

```bash
$ singularity exec <container> /usr/local/bin/compute_distance_all.py
$ podman run --it --rm --entrypoint /usr/local/bin/compute_distance_all.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute_distance_all.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dump_file.py

```bash
$ singularity exec <container> /usr/local/bin/dump_file.py
$ podman run --it --rm --entrypoint /usr/local/bin/dump_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dump_file.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_markers.py

```bash
$ singularity exec <container> /usr/local/bin/extract_markers.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_markers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_markers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx_len_filter.py

```bash
$ singularity exec <container> /usr/local/bin/fastx_len_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastx_len_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx_len_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_AF1.py

```bash
$ singularity exec <container> /usr/local/bin/fix_AF1.py
$ podman run --it --rm --entrypoint /usr/local/bin/fix_AF1.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_AF1.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_metaphlan_tables.py

```bash
$ singularity exec <container> /usr/local/bin/merge_metaphlan_tables.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_metaphlan_tables.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_metaphlan_tables.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaphlan2.py

```bash
$ singularity exec <container> /usr/local/bin/metaphlan2.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaphlan2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaphlan2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaphlan2krona.py

```bash
$ singularity exec <container> /usr/local/bin/metaphlan2krona.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaphlan2krona.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaphlan2krona.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mixed_utils.py

```bash
$ singularity exec <container> /usr/local/bin/mixed_utils.py
$ podman run --it --rm --entrypoint /usr/local/bin/mixed_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mixed_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ooSubprocess.py

```bash
$ singularity exec <container> /usr/local/bin/ooSubprocess.py
$ podman run --it --rm --entrypoint /usr/local/bin/ooSubprocess.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ooSubprocess.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_bug.py

```bash
$ singularity exec <container> /usr/local/bin/plot_bug.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_bug.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_bug.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_tree_ete2.py

```bash
$ singularity exec <container> /usr/local/bin/plot_tree_ete2.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_tree_ete2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_tree_ete2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_tree_graphlan.py

```bash
$ singularity exec <container> /usr/local/bin/plot_tree_graphlan.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_tree_graphlan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_tree_graphlan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_fastx.py

```bash
$ singularity exec <container> /usr/local/bin/read_fastx.py
$ podman run --it --rm --entrypoint /usr/local/bin/read_fastx.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_fastx.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_filter.py

```bash
$ singularity exec <container> /usr/local/bin/sam_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/sam_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sample2markers.py

```bash
$ singularity exec <container> /usr/local/bin/sample2markers.py
$ podman run --it --rm --entrypoint /usr/local/bin/sample2markers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sample2markers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strainphlan.py

```bash
$ singularity exec <container> /usr/local/bin/strainphlan.py
$ podman run --it --rm --entrypoint /usr/local/bin/strainphlan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strainphlan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### which.py

```bash
$ singularity exec <container> /usr/local/bin/which.py
$ podman run --it --rm --entrypoint /usr/local/bin/which.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/which.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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