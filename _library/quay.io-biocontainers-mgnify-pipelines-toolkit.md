---
layout: container
name:  "quay.io/biocontainers/mgnify-pipelines-toolkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mgnify-pipelines-toolkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mgnify-pipelines-toolkit/container.yaml"
updated_at: "2024-10-02 03:32:31.023457"
latest: "0.1.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mgnify-pipelines-toolkit"
aliases:
 - "are_there_primers"
 - "assess_inflection_point_mcp"
 - "assess_mcp_proportions"
 - "classify_var_regions"
 - "find_mcp_inflection_points"
 - "get_subunits"
 - "get_subunits_coords"
 - "make_asv_count_table"
 - "mapseq2biom"
 - "remove_ambiguous_reads"
 - "rev_comp_se_primers"
 - "standard_primer_matching"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
versions:
 - "0.1.0--pyhdfd78af_0"
 - "0.1.1--pyhdfd78af_0"
 - "0.1.2--pyhdfd78af_0"
 - "0.1.3--pyhdfd78af_0"
 - "0.1.4--pyhdfd78af_0"
 - "0.1.5--pyhdfd78af_0"
 - "0.1.6--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mgnify-pipelines-toolkit"
config: {"url": "https://biocontainers.pro/tools/mgnify-pipelines-toolkit", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mgnify-pipelines-toolkit", "latest": {"0.1.6--pyhdfd78af_0": "sha256:7c8c4d03269806a34da052ef0910df1a0a346de4c3a33428259ab7a9fcc2f9e6"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:2c88d8620818ec1a05a9943ea7328d1a4c10cbd5557756441e880ea511dbc7e0", "0.1.1--pyhdfd78af_0": "sha256:cff8ea49397260fb96f670e50d5aa1542ebb62d3a58760dee26cdcd9e0fa091f", "0.1.2--pyhdfd78af_0": "sha256:f8940745754cdaa2a5db03c045affdb8cde1573a0be1dade76cb049f8058bcd5", "0.1.3--pyhdfd78af_0": "sha256:cb63fdb3f112c9d7bff5a01142c858d875997aa542d0df84d7b44c3051c4fa18", "0.1.4--pyhdfd78af_0": "sha256:638693bd695c8543c244e108fbae04b3a74bab06d7c0ace52a00be1b071298a5", "0.1.5--pyhdfd78af_0": "sha256:72dd667296c3b620bf255ad2afc3bd685b04e6aaf745f3aaae65241cf719d73d", "0.1.6--pyhdfd78af_0": "sha256:7c8c4d03269806a34da052ef0910df1a0a346de4c3a33428259ab7a9fcc2f9e6"}, "docker": "quay.io/biocontainers/mgnify-pipelines-toolkit", "aliases": {"are_there_primers": "/usr/local/bin/are_there_primers", "assess_inflection_point_mcp": "/usr/local/bin/assess_inflection_point_mcp", "assess_mcp_proportions": "/usr/local/bin/assess_mcp_proportions", "classify_var_regions": "/usr/local/bin/classify_var_regions", "find_mcp_inflection_points": "/usr/local/bin/find_mcp_inflection_points", "get_subunits": "/usr/local/bin/get_subunits", "get_subunits_coords": "/usr/local/bin/get_subunits_coords", "make_asv_count_table": "/usr/local/bin/make_asv_count_table", "mapseq2biom": "/usr/local/bin/mapseq2biom", "remove_ambiguous_reads": "/usr/local/bin/remove_ambiguous_reads", "rev_comp_se_primers": "/usr/local/bin/rev_comp_se_primers", "standard_primer_matching": "/usr/local/bin/standard_primer_matching", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mgnify-pipelines-toolkit.
singularity registry hpc automated addition for mgnify-pipelines-toolkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mgnify-pipelines-toolkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mgnify-pipelines-toolkit:0.1.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mgnify-pipelines-toolkit/0.1.6--pyhdfd78af_0
$ module help quay.io/biocontainers/mgnify-pipelines-toolkit/0.1.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mgnify-pipelines-toolkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mgnify-pipelines-toolkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mgnify-pipelines-toolkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mgnify-pipelines-toolkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mgnify-pipelines-toolkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mgnify-pipelines-toolkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### are_there_primers

```bash
$ singularity exec <container> /usr/local/bin/are_there_primers
$ podman run --it --rm --entrypoint /usr/local/bin/are_there_primers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/are_there_primers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assess_inflection_point_mcp

```bash
$ singularity exec <container> /usr/local/bin/assess_inflection_point_mcp
$ podman run --it --rm --entrypoint /usr/local/bin/assess_inflection_point_mcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assess_inflection_point_mcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assess_mcp_proportions

```bash
$ singularity exec <container> /usr/local/bin/assess_mcp_proportions
$ podman run --it --rm --entrypoint /usr/local/bin/assess_mcp_proportions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assess_mcp_proportions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### classify_var_regions

```bash
$ singularity exec <container> /usr/local/bin/classify_var_regions
$ podman run --it --rm --entrypoint /usr/local/bin/classify_var_regions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/classify_var_regions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_mcp_inflection_points

```bash
$ singularity exec <container> /usr/local/bin/find_mcp_inflection_points
$ podman run --it --rm --entrypoint /usr/local/bin/find_mcp_inflection_points   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_mcp_inflection_points   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_subunits

```bash
$ singularity exec <container> /usr/local/bin/get_subunits
$ podman run --it --rm --entrypoint /usr/local/bin/get_subunits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_subunits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_subunits_coords

```bash
$ singularity exec <container> /usr/local/bin/get_subunits_coords
$ podman run --it --rm --entrypoint /usr/local/bin/get_subunits_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_subunits_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_asv_count_table

```bash
$ singularity exec <container> /usr/local/bin/make_asv_count_table
$ podman run --it --rm --entrypoint /usr/local/bin/make_asv_count_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_asv_count_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapseq2biom

```bash
$ singularity exec <container> /usr/local/bin/mapseq2biom
$ podman run --it --rm --entrypoint /usr/local/bin/mapseq2biom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapseq2biom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_ambiguous_reads

```bash
$ singularity exec <container> /usr/local/bin/remove_ambiguous_reads
$ podman run --it --rm --entrypoint /usr/local/bin/remove_ambiguous_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_ambiguous_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rev_comp_se_primers

```bash
$ singularity exec <container> /usr/local/bin/rev_comp_se_primers
$ podman run --it --rm --entrypoint /usr/local/bin/rev_comp_se_primers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rev_comp_se_primers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### standard_primer_matching

```bash
$ singularity exec <container> /usr/local/bin/standard_primer_matching
$ podman run --it --rm --entrypoint /usr/local/bin/standard_primer_matching   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/standard_primer_matching   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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