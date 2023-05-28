---
layout: container
name:  "quay.io/biocontainers/artic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/artic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/artic/container.yaml"
updated_at: "2023-05-28 03:27:14.772397"
latest: "1.2.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/artic"
aliases:
 - "align_trim"
 - "align_trim_n"
 - "artic"
 - "artic-tools"
 - "artic_fasta_header"
 - "artic_get_stats"
 - "artic_make_depth_mask"
 - "artic_mask"
 - "artic_vcf_filter"
 - "artic_vcf_merge"
 - "check_compression"
 - "compress_fast5"
 - "demux_fast5"
 - "fast5_subset"
 - "hdf2tf.py"
 - "longshot"
 - "margin_cons"
 - "margin_cons_medaka"
 - "medaka"
 - "medaka_consensus"
 - "medaka_counts"
 - "medaka_data_path"
 - "medaka_haploid_variant"
 - "medaka_version_report"
 - "mini_align"
 - "multi_to_single_fast5"
 - "nanopolish"
 - "nanopolish_makerange.py"
 - "nanopolish_merge.py"
 - "porechop"
 - "rich-click"
 - "single_to_multi_fast5"
 - "vcfextract"
 - "whatshap"
 - "multiqc"
 - "minimap2.py"
 - "racon"
 - "rampler"
 - "racon_wrapper"
 - "estimator_ckpt_converter"
 - "google-oauthlib-tool"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
versions:
 - "1.2.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for artic"
config: {"url": "https://biocontainers.pro/tools/artic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for artic", "latest": {"1.2.3--pyhdfd78af_0": "sha256:0576634dcbb7ae60090cd17f036002f8d825ff8185e5cbe6e2a9e6501e1f2a03"}, "tags": {"1.2.3--pyhdfd78af_0": "sha256:0576634dcbb7ae60090cd17f036002f8d825ff8185e5cbe6e2a9e6501e1f2a03"}, "docker": "quay.io/biocontainers/artic", "aliases": {"align_trim": "/usr/local/bin/align_trim", "align_trim_n": "/usr/local/bin/align_trim_n", "artic": "/usr/local/bin/artic", "artic-tools": "/usr/local/bin/artic-tools", "artic_fasta_header": "/usr/local/bin/artic_fasta_header", "artic_get_stats": "/usr/local/bin/artic_get_stats", "artic_make_depth_mask": "/usr/local/bin/artic_make_depth_mask", "artic_mask": "/usr/local/bin/artic_mask", "artic_vcf_filter": "/usr/local/bin/artic_vcf_filter", "artic_vcf_merge": "/usr/local/bin/artic_vcf_merge", "check_compression": "/usr/local/bin/check_compression", "compress_fast5": "/usr/local/bin/compress_fast5", "demux_fast5": "/usr/local/bin/demux_fast5", "fast5_subset": "/usr/local/bin/fast5_subset", "hdf2tf.py": "/usr/local/bin/hdf2tf.py", "longshot": "/usr/local/bin/longshot", "margin_cons": "/usr/local/bin/margin_cons", "margin_cons_medaka": "/usr/local/bin/margin_cons_medaka", "medaka": "/usr/local/bin/medaka", "medaka_consensus": "/usr/local/bin/medaka_consensus", "medaka_counts": "/usr/local/bin/medaka_counts", "medaka_data_path": "/usr/local/bin/medaka_data_path", "medaka_haploid_variant": "/usr/local/bin/medaka_haploid_variant", "medaka_version_report": "/usr/local/bin/medaka_version_report", "mini_align": "/usr/local/bin/mini_align", "multi_to_single_fast5": "/usr/local/bin/multi_to_single_fast5", "nanopolish": "/usr/local/bin/nanopolish", "nanopolish_makerange.py": "/usr/local/bin/nanopolish_makerange.py", "nanopolish_merge.py": "/usr/local/bin/nanopolish_merge.py", "porechop": "/usr/local/bin/porechop", "rich-click": "/usr/local/bin/rich-click", "single_to_multi_fast5": "/usr/local/bin/single_to_multi_fast5", "vcfextract": "/usr/local/bin/vcfextract", "whatshap": "/usr/local/bin/whatshap", "multiqc": "/usr/local/bin/multiqc", "minimap2.py": "/usr/local/bin/minimap2.py", "racon": "/usr/local/bin/racon", "rampler": "/usr/local/bin/rampler", "racon_wrapper": "/usr/local/bin/racon_wrapper", "estimator_ckpt_converter": "/usr/local/bin/estimator_ckpt_converter", "google-oauthlib-tool": "/usr/local/bin/google-oauthlib-tool", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/artic.
shpc-registry automated BioContainers addition for artic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/artic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/artic:1.2.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/artic/1.2.3--pyhdfd78af_0
$ module help quay.io/biocontainers/artic/1.2.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### artic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### artic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### artic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### artic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### artic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### artic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### align_trim

```bash
$ singularity exec <container> /usr/local/bin/align_trim
$ podman run --it --rm --entrypoint /usr/local/bin/align_trim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align_trim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align_trim_n

```bash
$ singularity exec <container> /usr/local/bin/align_trim_n
$ podman run --it --rm --entrypoint /usr/local/bin/align_trim_n   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align_trim_n   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### artic

```bash
$ singularity exec <container> /usr/local/bin/artic
$ podman run --it --rm --entrypoint /usr/local/bin/artic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/artic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### artic-tools

```bash
$ singularity exec <container> /usr/local/bin/artic-tools
$ podman run --it --rm --entrypoint /usr/local/bin/artic-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/artic-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### artic_fasta_header

```bash
$ singularity exec <container> /usr/local/bin/artic_fasta_header
$ podman run --it --rm --entrypoint /usr/local/bin/artic_fasta_header   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/artic_fasta_header   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### artic_get_stats

```bash
$ singularity exec <container> /usr/local/bin/artic_get_stats
$ podman run --it --rm --entrypoint /usr/local/bin/artic_get_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/artic_get_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### artic_make_depth_mask

```bash
$ singularity exec <container> /usr/local/bin/artic_make_depth_mask
$ podman run --it --rm --entrypoint /usr/local/bin/artic_make_depth_mask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/artic_make_depth_mask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### artic_mask

```bash
$ singularity exec <container> /usr/local/bin/artic_mask
$ podman run --it --rm --entrypoint /usr/local/bin/artic_mask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/artic_mask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### artic_vcf_filter

```bash
$ singularity exec <container> /usr/local/bin/artic_vcf_filter
$ podman run --it --rm --entrypoint /usr/local/bin/artic_vcf_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/artic_vcf_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### artic_vcf_merge

```bash
$ singularity exec <container> /usr/local/bin/artic_vcf_merge
$ podman run --it --rm --entrypoint /usr/local/bin/artic_vcf_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/artic_vcf_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### hdf2tf.py

```bash
$ singularity exec <container> /usr/local/bin/hdf2tf.py
$ podman run --it --rm --entrypoint /usr/local/bin/hdf2tf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf2tf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### longshot

```bash
$ singularity exec <container> /usr/local/bin/longshot
$ podman run --it --rm --entrypoint /usr/local/bin/longshot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/longshot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### margin_cons

```bash
$ singularity exec <container> /usr/local/bin/margin_cons
$ podman run --it --rm --entrypoint /usr/local/bin/margin_cons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/margin_cons   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### margin_cons_medaka

```bash
$ singularity exec <container> /usr/local/bin/margin_cons_medaka
$ podman run --it --rm --entrypoint /usr/local/bin/margin_cons_medaka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/margin_cons_medaka   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### medaka_haploid_variant

```bash
$ singularity exec <container> /usr/local/bin/medaka_haploid_variant
$ podman run --it --rm --entrypoint /usr/local/bin/medaka_haploid_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/medaka_haploid_variant   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### multi_to_single_fast5

```bash
$ singularity exec <container> /usr/local/bin/multi_to_single_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/multi_to_single_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi_to_single_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanopolish

```bash
$ singularity exec <container> /usr/local/bin/nanopolish
$ podman run --it --rm --entrypoint /usr/local/bin/nanopolish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanopolish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanopolish_makerange.py

```bash
$ singularity exec <container> /usr/local/bin/nanopolish_makerange.py
$ podman run --it --rm --entrypoint /usr/local/bin/nanopolish_makerange.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanopolish_makerange.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanopolish_merge.py

```bash
$ singularity exec <container> /usr/local/bin/nanopolish_merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/nanopolish_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanopolish_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### porechop

```bash
$ singularity exec <container> /usr/local/bin/porechop
$ podman run --it --rm --entrypoint /usr/local/bin/porechop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/porechop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### single_to_multi_fast5

```bash
$ singularity exec <container> /usr/local/bin/single_to_multi_fast5
$ podman run --it --rm --entrypoint /usr/local/bin/single_to_multi_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/single_to_multi_fast5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfextract

```bash
$ singularity exec <container> /usr/local/bin/vcfextract
$ podman run --it --rm --entrypoint /usr/local/bin/vcfextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### whatshap

```bash
$ singularity exec <container> /usr/local/bin/whatshap
$ podman run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiqc

```bash
$ singularity exec <container> /usr/local/bin/multiqc
$ podman run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2.py

```bash
$ singularity exec <container> /usr/local/bin/minimap2.py
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon

```bash
$ singularity exec <container> /usr/local/bin/racon
$ podman run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rampler

```bash
$ singularity exec <container> /usr/local/bin/rampler
$ podman run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon_wrapper

```bash
$ singularity exec <container> /usr/local/bin/racon_wrapper
$ podman run --it --rm --entrypoint /usr/local/bin/racon_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimator_ckpt_converter

```bash
$ singularity exec <container> /usr/local/bin/estimator_ckpt_converter
$ podman run --it --rm --entrypoint /usr/local/bin/estimator_ckpt_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimator_ckpt_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google-oauthlib-tool

```bash
$ singularity exec <container> /usr/local/bin/google-oauthlib-tool
$ podman run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_cpp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_cpp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_csharp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_csharp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_node_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_node_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
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