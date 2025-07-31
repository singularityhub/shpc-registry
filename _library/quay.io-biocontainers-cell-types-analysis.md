---
layout: container
name:  "quay.io/biocontainers/cell-types-analysis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cell-types-analysis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cell-types-analysis/container.yaml"
updated_at: "2025-07-31 11:14:17.869847"
latest: "0.1.11--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/cell-types-analysis"
aliases:
 - "bats"
 - "build_cell_ontology_dict.R"
 - "cell_types_utils.R"
 - "check_labels.R"
 - "combine_tool_outputs.R"
 - "downsample_cells.R"
 - "get_consensus_output.R"
 - "get_empirical_dist.R"
 - "get_tool_performance_table.R"
 - "get_tool_pvals.R"
 - "label_analysis_run_post_install_tests.bats"
 - "label_analysis_run_post_install_tests.sh"
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
 - "native2ascii"
 - "policytool"
 - "appletviewer"
 - "idlj"
 - "orbd"
versions:
 - "0.1.9--0"
 - "0.1.11--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for cell-types-analysis"
config: {"url": "https://biocontainers.pro/tools/cell-types-analysis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cell-types-analysis", "latest": {"0.1.11--hdfd78af_1": "sha256:330643417b81897cd9f8c20fb51f472394719bb55db31035224a582c2d3aeed7"}, "tags": {"0.1.9--0": "sha256:34f4133564860be6b6df7a6fc7b30829fe87391364ed11dddb62a3bfdbfcc022", "0.1.11--hdfd78af_1": "sha256:330643417b81897cd9f8c20fb51f472394719bb55db31035224a582c2d3aeed7"}, "docker": "quay.io/biocontainers/cell-types-analysis", "aliases": {"bats": "/usr/local/bin/bats", "build_cell_ontology_dict.R": "/usr/local/bin/build_cell_ontology_dict.R", "cell_types_utils.R": "/usr/local/bin/cell_types_utils.R", "check_labels.R": "/usr/local/bin/check_labels.R", "combine_tool_outputs.R": "/usr/local/bin/combine_tool_outputs.R", "downsample_cells.R": "/usr/local/bin/downsample_cells.R", "get_consensus_output.R": "/usr/local/bin/get_consensus_output.R", "get_empirical_dist.R": "/usr/local/bin/get_empirical_dist.R", "get_tool_performance_table.R": "/usr/local/bin/get_tool_performance_table.R", "get_tool_pvals.R": "/usr/local/bin/get_tool_pvals.R", "label_analysis_run_post_install_tests.bats": "/usr/local/bin/label_analysis_run_post_install_tests.bats", "label_analysis_run_post_install_tests.sh": "/usr/local/bin/label_analysis_run_post_install_tests.sh", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj", "orbd": "/usr/local/bin/orbd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cell-types-analysis.
shpc-registry automated BioContainers addition for cell-types-analysis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cell-types-analysis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cell-types-analysis:0.1.11--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cell-types-analysis/0.1.11--hdfd78af_1
$ module help quay.io/biocontainers/cell-types-analysis/0.1.11--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cell-types-analysis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cell-types-analysis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cell-types-analysis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cell-types-analysis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cell-types-analysis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cell-types-analysis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bats

```bash
$ singularity exec <container> /usr/local/bin/bats
$ podman run --it --rm --entrypoint /usr/local/bin/bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_cell_ontology_dict.R

```bash
$ singularity exec <container> /usr/local/bin/build_cell_ontology_dict.R
$ podman run --it --rm --entrypoint /usr/local/bin/build_cell_ontology_dict.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_cell_ontology_dict.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cell_types_utils.R

```bash
$ singularity exec <container> /usr/local/bin/cell_types_utils.R
$ podman run --it --rm --entrypoint /usr/local/bin/cell_types_utils.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cell_types_utils.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_labels.R

```bash
$ singularity exec <container> /usr/local/bin/check_labels.R
$ podman run --it --rm --entrypoint /usr/local/bin/check_labels.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_labels.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_tool_outputs.R

```bash
$ singularity exec <container> /usr/local/bin/combine_tool_outputs.R
$ podman run --it --rm --entrypoint /usr/local/bin/combine_tool_outputs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_tool_outputs.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### downsample_cells.R

```bash
$ singularity exec <container> /usr/local/bin/downsample_cells.R
$ podman run --it --rm --entrypoint /usr/local/bin/downsample_cells.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/downsample_cells.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_consensus_output.R

```bash
$ singularity exec <container> /usr/local/bin/get_consensus_output.R
$ podman run --it --rm --entrypoint /usr/local/bin/get_consensus_output.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_consensus_output.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_empirical_dist.R

```bash
$ singularity exec <container> /usr/local/bin/get_empirical_dist.R
$ podman run --it --rm --entrypoint /usr/local/bin/get_empirical_dist.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_empirical_dist.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_tool_performance_table.R

```bash
$ singularity exec <container> /usr/local/bin/get_tool_performance_table.R
$ podman run --it --rm --entrypoint /usr/local/bin/get_tool_performance_table.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_tool_performance_table.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_tool_pvals.R

```bash
$ singularity exec <container> /usr/local/bin/get_tool_pvals.R
$ podman run --it --rm --entrypoint /usr/local/bin/get_tool_pvals.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_tool_pvals.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### label_analysis_run_post_install_tests.bats

```bash
$ singularity exec <container> /usr/local/bin/label_analysis_run_post_install_tests.bats
$ podman run --it --rm --entrypoint /usr/local/bin/label_analysis_run_post_install_tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/label_analysis_run_post_install_tests.bats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### label_analysis_run_post_install_tests.sh

```bash
$ singularity exec <container> /usr/local/bin/label_analysis_run_post_install_tests.sh
$ podman run --it --rm --entrypoint /usr/local/bin/label_analysis_run_post_install_tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/label_analysis_run_post_install_tests.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javah

```bash
$ singularity exec <container> /usr/local/bin/javah
$ podman run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhat

```bash
$ singularity exec <container> /usr/local/bin/jhat
$ podman run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsadebugd

```bash
$ singularity exec <container> /usr/local/bin/jsadebugd
$ podman run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### native2ascii

```bash
$ singularity exec <container> /usr/local/bin/native2ascii
$ podman run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### policytool

```bash
$ singularity exec <container> /usr/local/bin/policytool
$ podman run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idlj

```bash
$ singularity exec <container> /usr/local/bin/idlj
$ podman run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orbd

```bash
$ singularity exec <container> /usr/local/bin/orbd
$ podman run --it --rm --entrypoint /usr/local/bin/orbd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orbd   -v ${PWD} -w ${PWD} <container> -c " $@"
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