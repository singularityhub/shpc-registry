---
layout: container
name:  "quay.io/biocontainers/snvphyl-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snvphyl-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snvphyl-tools/container.yaml"
updated_at: "2025-10-03 03:31:30.983377"
latest: "1.8.2--pl5321h7b50bb2_9"
container_url: "https://biocontainers.pro/tools/snvphyl-tools"
aliases:
 - "consolidate_vcfs.pl"
 - "core-only.pl"
 - "extract_snvs_metaalign.pl"
 - "filter-positions.pl"
 - "filter-stats.pl"
 - "filterVcf.pl"
 - "filter_unique_basepairs.pl"
 - "find-positions-used.pl"
 - "find-repeats.pl"
 - "positions2phyloviz.pl"
 - "positions2snv_alignment.pl"
 - "positions2snv_invariant_alignment.pl"
 - "rearrange_snv_matrix.pl"
 - "ref_stats.pl"
 - "reporter.pl"
 - "snv_matrix.pl"
 - "tab-to-vcf"
 - "tsvToVcf.pl"
 - "vcf-haplotypes"
 - "vcf2snv_alignment.pl"
 - "vcftools"
 - "verify_excess_coverage.pl"
 - "verify_low_depth.pl"
 - "verify_mapping_quality.pl"
 - "fill-aa"
 - "fill-an-ac"
 - "fill-fs"
 - "fill-ref-md5"
 - "vcf-annotate"
 - "vcf-compare"
 - "vcf-concat"
 - "vcf-consensus"
 - "vcf-contrast"
 - "vcf-convert"
versions:
 - "1.8.2--pl5321hec16e2b_7"
 - "1.8.2--pl5321h031d066_8"
 - "1.8.2--pl5321h7b50bb2_9"
description: "shpc-registry automated BioContainers addition for snvphyl-tools"
config: {"url": "https://biocontainers.pro/tools/snvphyl-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snvphyl-tools", "latest": {"1.8.2--pl5321h7b50bb2_9": "sha256:2bfb8fc596a49e6e746d83e050e821bd8f0128cd424957dc72145cd4e58cd15c"}, "tags": {"1.8.2--pl5321hec16e2b_7": "sha256:fe1f048582277dc804e194a3dab05e8e7f1286478b04d01af204733932d8cca9", "1.8.2--pl5321h031d066_8": "sha256:7596eefba724af0f222d6e326f9262ef569c64983153ff8204c9ec93a683a555", "1.8.2--pl5321h7b50bb2_9": "sha256:2bfb8fc596a49e6e746d83e050e821bd8f0128cd424957dc72145cd4e58cd15c"}, "docker": "quay.io/biocontainers/snvphyl-tools", "aliases": {"consolidate_vcfs.pl": "/usr/local/bin/consolidate_vcfs.pl", "core-only.pl": "/usr/local/bin/core-only.pl", "extract_snvs_metaalign.pl": "/usr/local/bin/extract_snvs_metaalign.pl", "filter-positions.pl": "/usr/local/bin/filter-positions.pl", "filter-stats.pl": "/usr/local/bin/filter-stats.pl", "filterVcf.pl": "/usr/local/bin/filterVcf.pl", "filter_unique_basepairs.pl": "/usr/local/bin/filter_unique_basepairs.pl", "find-positions-used.pl": "/usr/local/bin/find-positions-used.pl", "find-repeats.pl": "/usr/local/bin/find-repeats.pl", "positions2phyloviz.pl": "/usr/local/bin/positions2phyloviz.pl", "positions2snv_alignment.pl": "/usr/local/bin/positions2snv_alignment.pl", "positions2snv_invariant_alignment.pl": "/usr/local/bin/positions2snv_invariant_alignment.pl", "rearrange_snv_matrix.pl": "/usr/local/bin/rearrange_snv_matrix.pl", "ref_stats.pl": "/usr/local/bin/ref_stats.pl", "reporter.pl": "/usr/local/bin/reporter.pl", "snv_matrix.pl": "/usr/local/bin/snv_matrix.pl", "tab-to-vcf": "/usr/local/bin/tab-to-vcf", "tsvToVcf.pl": "/usr/local/bin/tsvToVcf.pl", "vcf-haplotypes": "/usr/local/bin/vcf-haplotypes", "vcf2snv_alignment.pl": "/usr/local/bin/vcf2snv_alignment.pl", "vcftools": "/usr/local/bin/vcftools", "verify_excess_coverage.pl": "/usr/local/bin/verify_excess_coverage.pl", "verify_low_depth.pl": "/usr/local/bin/verify_low_depth.pl", "verify_mapping_quality.pl": "/usr/local/bin/verify_mapping_quality.pl", "fill-aa": "/usr/local/bin/fill-aa", "fill-an-ac": "/usr/local/bin/fill-an-ac", "fill-fs": "/usr/local/bin/fill-fs", "fill-ref-md5": "/usr/local/bin/fill-ref-md5", "vcf-annotate": "/usr/local/bin/vcf-annotate", "vcf-compare": "/usr/local/bin/vcf-compare", "vcf-concat": "/usr/local/bin/vcf-concat", "vcf-consensus": "/usr/local/bin/vcf-consensus", "vcf-contrast": "/usr/local/bin/vcf-contrast", "vcf-convert": "/usr/local/bin/vcf-convert"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snvphyl-tools.
shpc-registry automated BioContainers addition for snvphyl-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snvphyl-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snvphyl-tools:1.8.2--pl5321h7b50bb2_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snvphyl-tools/1.8.2--pl5321h7b50bb2_9
$ module help quay.io/biocontainers/snvphyl-tools/1.8.2--pl5321h7b50bb2_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snvphyl-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snvphyl-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snvphyl-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snvphyl-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snvphyl-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snvphyl-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### consolidate_vcfs.pl

```bash
$ singularity exec <container> /usr/local/bin/consolidate_vcfs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/consolidate_vcfs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consolidate_vcfs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### core-only.pl

```bash
$ singularity exec <container> /usr/local/bin/core-only.pl
$ podman run --it --rm --entrypoint /usr/local/bin/core-only.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/core-only.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_snvs_metaalign.pl

```bash
$ singularity exec <container> /usr/local/bin/extract_snvs_metaalign.pl
$ podman run --it --rm --entrypoint /usr/local/bin/extract_snvs_metaalign.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_snvs_metaalign.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-positions.pl

```bash
$ singularity exec <container> /usr/local/bin/filter-positions.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter-positions.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-positions.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-stats.pl

```bash
$ singularity exec <container> /usr/local/bin/filter-stats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter-stats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-stats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterVcf.pl

```bash
$ singularity exec <container> /usr/local/bin/filterVcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filterVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_unique_basepairs.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_unique_basepairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_unique_basepairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_unique_basepairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-positions-used.pl

```bash
$ singularity exec <container> /usr/local/bin/find-positions-used.pl
$ podman run --it --rm --entrypoint /usr/local/bin/find-positions-used.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-positions-used.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-repeats.pl

```bash
$ singularity exec <container> /usr/local/bin/find-repeats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/find-repeats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-repeats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### positions2phyloviz.pl

```bash
$ singularity exec <container> /usr/local/bin/positions2phyloviz.pl
$ podman run --it --rm --entrypoint /usr/local/bin/positions2phyloviz.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/positions2phyloviz.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### positions2snv_alignment.pl

```bash
$ singularity exec <container> /usr/local/bin/positions2snv_alignment.pl
$ podman run --it --rm --entrypoint /usr/local/bin/positions2snv_alignment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/positions2snv_alignment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### positions2snv_invariant_alignment.pl

```bash
$ singularity exec <container> /usr/local/bin/positions2snv_invariant_alignment.pl
$ podman run --it --rm --entrypoint /usr/local/bin/positions2snv_invariant_alignment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/positions2snv_invariant_alignment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rearrange_snv_matrix.pl

```bash
$ singularity exec <container> /usr/local/bin/rearrange_snv_matrix.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rearrange_snv_matrix.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rearrange_snv_matrix.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref_stats.pl

```bash
$ singularity exec <container> /usr/local/bin/ref_stats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ref_stats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref_stats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reporter.pl

```bash
$ singularity exec <container> /usr/local/bin/reporter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/reporter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reporter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snv_matrix.pl

```bash
$ singularity exec <container> /usr/local/bin/snv_matrix.pl
$ podman run --it --rm --entrypoint /usr/local/bin/snv_matrix.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snv_matrix.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tab-to-vcf

```bash
$ singularity exec <container> /usr/local/bin/tab-to-vcf
$ podman run --it --rm --entrypoint /usr/local/bin/tab-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tab-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsvToVcf.pl

```bash
$ singularity exec <container> /usr/local/bin/tsvToVcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/tsvToVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsvToVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-haplotypes

```bash
$ singularity exec <container> /usr/local/bin/vcf-haplotypes
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-haplotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-haplotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2snv_alignment.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2snv_alignment.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2snv_alignment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2snv_alignment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcftools

```bash
$ singularity exec <container> /usr/local/bin/vcftools
$ podman run --it --rm --entrypoint /usr/local/bin/vcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### verify_excess_coverage.pl

```bash
$ singularity exec <container> /usr/local/bin/verify_excess_coverage.pl
$ podman run --it --rm --entrypoint /usr/local/bin/verify_excess_coverage.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/verify_excess_coverage.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### verify_low_depth.pl

```bash
$ singularity exec <container> /usr/local/bin/verify_low_depth.pl
$ podman run --it --rm --entrypoint /usr/local/bin/verify_low_depth.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/verify_low_depth.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### verify_mapping_quality.pl

```bash
$ singularity exec <container> /usr/local/bin/verify_mapping_quality.pl
$ podman run --it --rm --entrypoint /usr/local/bin/verify_mapping_quality.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/verify_mapping_quality.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-aa

```bash
$ singularity exec <container> /usr/local/bin/fill-aa
$ podman run --it --rm --entrypoint /usr/local/bin/fill-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-an-ac

```bash
$ singularity exec <container> /usr/local/bin/fill-an-ac
$ podman run --it --rm --entrypoint /usr/local/bin/fill-an-ac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-an-ac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-fs

```bash
$ singularity exec <container> /usr/local/bin/fill-fs
$ podman run --it --rm --entrypoint /usr/local/bin/fill-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-ref-md5

```bash
$ singularity exec <container> /usr/local/bin/fill-ref-md5
$ podman run --it --rm --entrypoint /usr/local/bin/fill-ref-md5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-ref-md5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-annotate

```bash
$ singularity exec <container> /usr/local/bin/vcf-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-compare

```bash
$ singularity exec <container> /usr/local/bin/vcf-compare
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-concat

```bash
$ singularity exec <container> /usr/local/bin/vcf-concat
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-consensus

```bash
$ singularity exec <container> /usr/local/bin/vcf-consensus
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-contrast

```bash
$ singularity exec <container> /usr/local/bin/vcf-contrast
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-convert

```bash
$ singularity exec <container> /usr/local/bin/vcf-convert
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
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