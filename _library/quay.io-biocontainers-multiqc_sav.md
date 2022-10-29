---
layout: container
name:  "quay.io/biocontainers/multiqc_sav"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/multiqc_sav/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/multiqc_sav/container.yaml"
updated_at: "2022-10-29 05:31:07.853429"
latest: "0.0.3--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/multiqc_sav"
aliases:
 - "interop_aggregate"
 - "interop_dumpbin"
 - "interop_dumptext"
 - "interop_imaging_table"
 - "interop_index-summary"
 - "interop_plot_by_cycle"
 - "interop_plot_by_lane"
 - "interop_plot_flowcell"
 - "interop_plot_qscore_heatmap"
 - "interop_plot_qscore_histogram"
 - "interop_plot_sample_qc"
 - "interop_summary"
 - "2to3-3.10"
 - "brotli"
 - "cmark"
 - "coloredlogs"
 - "cwebp"
 - "dwebp"
 - "f2py3.10"
 - "fonttools"
 - "futurize"
 - "gif2rgb"
versions:
 - "0.0.3--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for multiqc_sav"
config: {"url": "https://biocontainers.pro/tools/multiqc_sav", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for multiqc_sav", "latest": {"0.0.3--pyh5e36f6f_0": "sha256:af63bf97d223419b2d492ff950433d43b767146ef1b1ec76f0a0be2839014896"}, "tags": {"0.0.3--pyh5e36f6f_0": "sha256:af63bf97d223419b2d492ff950433d43b767146ef1b1ec76f0a0be2839014896"}, "docker": "quay.io/biocontainers/multiqc_sav", "aliases": {"interop_aggregate": "/usr/local/bin/interop_aggregate", "interop_dumpbin": "/usr/local/bin/interop_dumpbin", "interop_dumptext": "/usr/local/bin/interop_dumptext", "interop_imaging_table": "/usr/local/bin/interop_imaging_table", "interop_index-summary": "/usr/local/bin/interop_index-summary", "interop_plot_by_cycle": "/usr/local/bin/interop_plot_by_cycle", "interop_plot_by_lane": "/usr/local/bin/interop_plot_by_lane", "interop_plot_flowcell": "/usr/local/bin/interop_plot_flowcell", "interop_plot_qscore_heatmap": "/usr/local/bin/interop_plot_qscore_heatmap", "interop_plot_qscore_histogram": "/usr/local/bin/interop_plot_qscore_histogram", "interop_plot_sample_qc": "/usr/local/bin/interop_plot_sample_qc", "interop_summary": "/usr/local/bin/interop_summary", "2to3-3.10": "/usr/local/bin/2to3-3.10", "brotli": "/usr/local/bin/brotli", "cmark": "/usr/local/bin/cmark", "coloredlogs": "/usr/local/bin/coloredlogs", "cwebp": "/usr/local/bin/cwebp", "dwebp": "/usr/local/bin/dwebp", "f2py3.10": "/usr/local/bin/f2py3.10", "fonttools": "/usr/local/bin/fonttools", "futurize": "/usr/local/bin/futurize", "gif2rgb": "/usr/local/bin/gif2rgb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/multiqc_sav.
shpc-registry automated BioContainers addition for multiqc_sav
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/multiqc_sav
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/multiqc_sav:0.0.3--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/multiqc_sav/0.0.3--pyh5e36f6f_0
$ module help quay.io/biocontainers/multiqc_sav/0.0.3--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### multiqc_sav-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### multiqc_sav-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### multiqc_sav-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### multiqc_sav-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### multiqc_sav-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### multiqc_sav-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### interop_aggregate

```bash
$ singularity exec <container> /usr/local/bin/interop_aggregate
$ podman run --it --rm --entrypoint /usr/local/bin/interop_aggregate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_aggregate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_dumpbin

```bash
$ singularity exec <container> /usr/local/bin/interop_dumpbin
$ podman run --it --rm --entrypoint /usr/local/bin/interop_dumpbin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_dumpbin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_dumptext

```bash
$ singularity exec <container> /usr/local/bin/interop_dumptext
$ podman run --it --rm --entrypoint /usr/local/bin/interop_dumptext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_dumptext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_imaging_table

```bash
$ singularity exec <container> /usr/local/bin/interop_imaging_table
$ podman run --it --rm --entrypoint /usr/local/bin/interop_imaging_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_imaging_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_index-summary

```bash
$ singularity exec <container> /usr/local/bin/interop_index-summary
$ podman run --it --rm --entrypoint /usr/local/bin/interop_index-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_index-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_plot_by_cycle

```bash
$ singularity exec <container> /usr/local/bin/interop_plot_by_cycle
$ podman run --it --rm --entrypoint /usr/local/bin/interop_plot_by_cycle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_plot_by_cycle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_plot_by_lane

```bash
$ singularity exec <container> /usr/local/bin/interop_plot_by_lane
$ podman run --it --rm --entrypoint /usr/local/bin/interop_plot_by_lane   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_plot_by_lane   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_plot_flowcell

```bash
$ singularity exec <container> /usr/local/bin/interop_plot_flowcell
$ podman run --it --rm --entrypoint /usr/local/bin/interop_plot_flowcell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_plot_flowcell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_plot_qscore_heatmap

```bash
$ singularity exec <container> /usr/local/bin/interop_plot_qscore_heatmap
$ podman run --it --rm --entrypoint /usr/local/bin/interop_plot_qscore_heatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_plot_qscore_heatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_plot_qscore_histogram

```bash
$ singularity exec <container> /usr/local/bin/interop_plot_qscore_histogram
$ podman run --it --rm --entrypoint /usr/local/bin/interop_plot_qscore_histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_plot_qscore_histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_plot_sample_qc

```bash
$ singularity exec <container> /usr/local/bin/interop_plot_sample_qc
$ podman run --it --rm --entrypoint /usr/local/bin/interop_plot_sample_qc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_plot_sample_qc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_summary

```bash
$ singularity exec <container> /usr/local/bin/interop_summary
$ podman run --it --rm --entrypoint /usr/local/bin/interop_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwebp

```bash
$ singularity exec <container> /usr/local/bin/dwebp
$ podman run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2rgb

```bash
$ singularity exec <container> /usr/local/bin/gif2rgb
$ podman run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
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