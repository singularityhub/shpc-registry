---
layout: container
name:  "quay.io/biocontainers/ssuissero"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ssuissero/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ssuissero/container.yaml"
updated_at: "2024-01-08 03:10:17.745053"
latest: "1.0.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/ssuissero"
aliases:
 - "SsuisSero.sh"
 - "check_compression"
 - "compress_fast5"
 - "demux_fast5"
 - "fast5_subset"
 - "flye"
 - "flye-minimap2"
 - "flye-modules"
 - "flye-samtools"
 - "medaka"
 - "medaka_consensus"
 - "medaka_counts"
 - "medaka_data_path"
 - "medaka_variant"
 - "medaka_version_report"
 - "mini_align"
 - "minipolish"
 - "multi_to_single_fast5"
 - "single_to_multi_fast5"
 - "vcfnormalizesvs"
 - "vcfnull2ref"
 - "vcfunphase"
 - "whatshap"
 - "minimap2.py"
 - "plotBfst.R"
 - "plotHapLrt.R"
 - "plotHaplotypes.R"
 - "plotPfst.R"
 - "plotSmoothed.R"
 - "plotWCfst.R"
 - "plotXPEHH.R"
 - "plot_roc.r"
 - "racon"
versions:
 - "1.0.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for ssuissero"
config: {"url": "https://biocontainers.pro/tools/ssuissero", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ssuissero", "latest": {"1.0.1--hdfd78af_1": "sha256:f745fb165d5376b1fd8bcde06b7a20b066efa4c8cafbdba05e37646099aa9082"}, "tags": {"1.0.1--hdfd78af_1": "sha256:f745fb165d5376b1fd8bcde06b7a20b066efa4c8cafbdba05e37646099aa9082"}, "docker": "quay.io/biocontainers/ssuissero", "aliases": {"SsuisSero.sh": "/usr/local/bin/SsuisSero.sh", "check_compression": "/usr/local/bin/check_compression", "compress_fast5": "/usr/local/bin/compress_fast5", "demux_fast5": "/usr/local/bin/demux_fast5", "fast5_subset": "/usr/local/bin/fast5_subset", "flye": "/usr/local/bin/flye", "flye-minimap2": "/usr/local/bin/flye-minimap2", "flye-modules": "/usr/local/bin/flye-modules", "flye-samtools": "/usr/local/bin/flye-samtools", "medaka": "/usr/local/bin/medaka", "medaka_consensus": "/usr/local/bin/medaka_consensus", "medaka_counts": "/usr/local/bin/medaka_counts", "medaka_data_path": "/usr/local/bin/medaka_data_path", "medaka_variant": "/usr/local/bin/medaka_variant", "medaka_version_report": "/usr/local/bin/medaka_version_report", "mini_align": "/usr/local/bin/mini_align", "minipolish": "/usr/local/bin/minipolish", "multi_to_single_fast5": "/usr/local/bin/multi_to_single_fast5", "single_to_multi_fast5": "/usr/local/bin/single_to_multi_fast5", "vcfnormalizesvs": "/usr/local/bin/vcfnormalizesvs", "vcfnull2ref": "/usr/local/bin/vcfnull2ref", "vcfunphase": "/usr/local/bin/vcfunphase", "whatshap": "/usr/local/bin/whatshap", "minimap2.py": "/usr/local/bin/minimap2.py", "plotBfst.R": "/usr/local/bin/plotBfst.R", "plotHapLrt.R": "/usr/local/bin/plotHapLrt.R", "plotHaplotypes.R": "/usr/local/bin/plotHaplotypes.R", "plotPfst.R": "/usr/local/bin/plotPfst.R", "plotSmoothed.R": "/usr/local/bin/plotSmoothed.R", "plotWCfst.R": "/usr/local/bin/plotWCfst.R", "plotXPEHH.R": "/usr/local/bin/plotXPEHH.R", "plot_roc.r": "/usr/local/bin/plot_roc.r", "racon": "/usr/local/bin/racon"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ssuissero.
shpc-registry automated BioContainers addition for ssuissero
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ssuissero
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ssuissero:1.0.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ssuissero/1.0.1--hdfd78af_1
$ module help quay.io/biocontainers/ssuissero/1.0.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ssuissero-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ssuissero-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ssuissero-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ssuissero-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ssuissero-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ssuissero-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SsuisSero.sh

```bash
$ singularity exec <container> /usr/local/bin/SsuisSero.sh
$ podman run --it --rm --entrypoint /usr/local/bin/SsuisSero.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SsuisSero.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_compression

```bash
$ singularity exec <container> /usr/local/bin/check_compression
$ podman run --it --rm --entrypoint /usr/local/bin/check_compression   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_compression   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compress_fast5

```bash
$ singularity exec <container> /usr/local/bin/compress_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/compress_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compress_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demux_fast5

```bash
$ singularity exec <container> /usr/local/bin/demux_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/demux_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demux_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fast5_subset

```bash
$ singularity exec <container> /usr/local/bin/fast5_subset
$ podman run --it --rm --entrypoint /usr/local/bin/fast5_subset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast5_subset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye

```bash
$ singularity exec <container> /usr/local/bin/flye
$ podman run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-minimap2

```bash
$ singularity exec <container> /usr/local/bin/flye-minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-modules

```bash
$ singularity exec <container> /usr/local/bin/flye-modules
$ podman run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-samtools

```bash
$ singularity exec <container> /usr/local/bin/flye-samtools
$ podman run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka

```bash
$ singularity exec <container> /usr/local/bin/medaka
$ podman run --it --rm --entrypoint /usr/local/bin/medaka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_consensus

```bash
$ singularity exec <container> /usr/local/bin/medaka_consensus
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_counts

```bash
$ singularity exec <container> /usr/local/bin/medaka_counts
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_counts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_counts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_data_path

```bash
$ singularity exec <container> /usr/local/bin/medaka_data_path
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_data_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_data_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_variant

```bash
$ singularity exec <container> /usr/local/bin/medaka_variant
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### medaka_version_report

```bash
$ singularity exec <container> /usr/local/bin/medaka_version_report
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_version_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_version_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mini_align

```bash
$ singularity exec <container> /usr/local/bin/mini_align
$ podman run --it --rm --entrypoint /usr/local/bin/mini_align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mini_align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minipolish

```bash
$ singularity exec <container> /usr/local/bin/minipolish
$ podman run --it --rm --entrypoint /usr/local/bin/minipolish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minipolish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi_to_single_fast5

```bash
$ singularity exec <container> /usr/local/bin/multi_to_single_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/multi_to_single_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi_to_single_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### single_to_multi_fast5

```bash
$ singularity exec <container> /usr/local/bin/single_to_multi_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/single_to_multi_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/single_to_multi_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfnormalizesvs

```bash
$ singularity exec <container> /usr/local/bin/vcfnormalizesvs
$ podman run --it --rm --entrypoint /usr/local/bin/vcfnormalizesvs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfnormalizesvs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfnull2ref

```bash
$ singularity exec <container> /usr/local/bin/vcfnull2ref
$ podman run --it --rm --entrypoint /usr/local/bin/vcfnull2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfnull2ref   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfunphase

```bash
$ singularity exec <container> /usr/local/bin/vcfunphase
$ podman run --it --rm --entrypoint /usr/local/bin/vcfunphase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfunphase   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### whatshap

```bash
$ singularity exec <container> /usr/local/bin/whatshap
$ podman run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2.py

```bash
$ singularity exec <container> /usr/local/bin/minimap2.py
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotBfst.R

```bash
$ singularity exec <container> /usr/local/bin/plotBfst.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotBfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotBfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotHapLrt.R

```bash
$ singularity exec <container> /usr/local/bin/plotHapLrt.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotHapLrt.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotHapLrt.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotHaplotypes.R

```bash
$ singularity exec <container> /usr/local/bin/plotHaplotypes.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotHaplotypes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotHaplotypes.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotPfst.R

```bash
$ singularity exec <container> /usr/local/bin/plotPfst.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotPfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotPfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotSmoothed.R

```bash
$ singularity exec <container> /usr/local/bin/plotSmoothed.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotSmoothed.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotSmoothed.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotWCfst.R

```bash
$ singularity exec <container> /usr/local/bin/plotWCfst.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotWCfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotWCfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotXPEHH.R

```bash
$ singularity exec <container> /usr/local/bin/plotXPEHH.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotXPEHH.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotXPEHH.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_roc.r

```bash
$ singularity exec <container> /usr/local/bin/plot_roc.r
$ podman run --it --rm --entrypoint /usr/local/bin/plot_roc.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_roc.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon

```bash
$ singularity exec <container> /usr/local/bin/racon
$ podman run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
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