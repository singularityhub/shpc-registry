---
layout: container
name:  "quay.io/biocontainers/linkedsv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/linkedsv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/linkedsv/container.yaml"
updated_at: "2025-09-02 03:38:21.992436"
latest: "0.1.0--h077b44d_0"
container_url: "https://biocontainers.pro/tools/linkedsv"
aliases:
 - "bfc"
 - "cal_2d_overlapping_barcodes"
 - "cal_barcode_depth_from_bcd21"
 - "cal_centroid_from_read_depth"
 - "cal_hap_read_depth_from_bcd21"
 - "cal_read_depth_from_bcd21"
 - "cal_twin_win_bcd_cnt"
 - "cluster_reads"
 - "cnv_detection"
 - "extract_barcode_info"
 - "fermi2"
 - "fermi2.pl"
 - "grid_overlap"
 - "hapdip.js"
 - "htsbox"
 - "linkedsv.py"
 - "output_bam_coreinfo"
 - "remove_sparse_nodes"
 - "ropebwt2"
 - "run-calling"
 - "small_deletion_detection"
 - "trimadap"
 - "trimadap-mt"
 - "perl5.22.0"
 - "seqtk"
 - "c2ph"
 - "pstruct"
 - "annot-tsv"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "numpy-config"
 - "pigz"
 - "unpigz"
 - "bwa"
 - "k8"
 - "shiftBed"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
 - "bedtools"
versions:
 - "0.1.0--h077b44d_0"
description: "singularity registry hpc automated addition for linkedsv"
config: {"url": "https://biocontainers.pro/tools/linkedsv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for linkedsv", "latest": {"0.1.0--h077b44d_0": "sha256:afc1cc2f7d36f313c6d9e03ce2304a0232739223caa085587ca0026d561b9960"}, "tags": {"0.1.0--h077b44d_0": "sha256:afc1cc2f7d36f313c6d9e03ce2304a0232739223caa085587ca0026d561b9960"}, "docker": "quay.io/biocontainers/linkedsv", "aliases": {"bfc": "/usr/local/bin/bfc", "cal_2d_overlapping_barcodes": "/usr/local/bin/cal_2d_overlapping_barcodes", "cal_barcode_depth_from_bcd21": "/usr/local/bin/cal_barcode_depth_from_bcd21", "cal_centroid_from_read_depth": "/usr/local/bin/cal_centroid_from_read_depth", "cal_hap_read_depth_from_bcd21": "/usr/local/bin/cal_hap_read_depth_from_bcd21", "cal_read_depth_from_bcd21": "/usr/local/bin/cal_read_depth_from_bcd21", "cal_twin_win_bcd_cnt": "/usr/local/bin/cal_twin_win_bcd_cnt", "cluster_reads": "/usr/local/bin/cluster_reads", "cnv_detection": "/usr/local/bin/cnv_detection", "extract_barcode_info": "/usr/local/bin/extract_barcode_info", "fermi2": "/usr/local/bin/fermi2", "fermi2.pl": "/usr/local/bin/fermi2.pl", "grid_overlap": "/usr/local/bin/grid_overlap", "hapdip.js": "/usr/local/bin/hapdip.js", "htsbox": "/usr/local/bin/htsbox", "linkedsv.py": "/usr/local/bin/linkedsv.py", "output_bam_coreinfo": "/usr/local/bin/output_bam_coreinfo", "remove_sparse_nodes": "/usr/local/bin/remove_sparse_nodes", "ropebwt2": "/usr/local/bin/ropebwt2", "run-calling": "/usr/local/bin/run-calling", "small_deletion_detection": "/usr/local/bin/small_deletion_detection", "trimadap": "/usr/local/bin/trimadap", "trimadap-mt": "/usr/local/bin/trimadap-mt", "perl5.22.0": "/usr/local/bin/perl5.22.0", "seqtk": "/usr/local/bin/seqtk", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "annot-tsv": "/usr/local/bin/annot-tsv", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "numpy-config": "/usr/local/bin/numpy-config", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "bwa": "/usr/local/bin/bwa", "k8": "/usr/local/bin/k8", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/linkedsv.
singularity registry hpc automated addition for linkedsv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/linkedsv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/linkedsv:0.1.0--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/linkedsv/0.1.0--h077b44d_0
$ module help quay.io/biocontainers/linkedsv/0.1.0--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### linkedsv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### linkedsv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### linkedsv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### linkedsv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### linkedsv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### linkedsv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bfc

```bash
$ singularity exec <container> /usr/local/bin/bfc
$ podman run --it --rm --entrypoint /usr/local/bin/bfc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bfc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cal_2d_overlapping_barcodes

```bash
$ singularity exec <container> /usr/local/bin/cal_2d_overlapping_barcodes
$ podman run --it --rm --entrypoint /usr/local/bin/cal_2d_overlapping_barcodes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cal_2d_overlapping_barcodes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cal_barcode_depth_from_bcd21

```bash
$ singularity exec <container> /usr/local/bin/cal_barcode_depth_from_bcd21
$ podman run --it --rm --entrypoint /usr/local/bin/cal_barcode_depth_from_bcd21   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cal_barcode_depth_from_bcd21   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cal_centroid_from_read_depth

```bash
$ singularity exec <container> /usr/local/bin/cal_centroid_from_read_depth
$ podman run --it --rm --entrypoint /usr/local/bin/cal_centroid_from_read_depth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cal_centroid_from_read_depth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cal_hap_read_depth_from_bcd21

```bash
$ singularity exec <container> /usr/local/bin/cal_hap_read_depth_from_bcd21
$ podman run --it --rm --entrypoint /usr/local/bin/cal_hap_read_depth_from_bcd21   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cal_hap_read_depth_from_bcd21   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cal_read_depth_from_bcd21

```bash
$ singularity exec <container> /usr/local/bin/cal_read_depth_from_bcd21
$ podman run --it --rm --entrypoint /usr/local/bin/cal_read_depth_from_bcd21   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cal_read_depth_from_bcd21   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cal_twin_win_bcd_cnt

```bash
$ singularity exec <container> /usr/local/bin/cal_twin_win_bcd_cnt
$ podman run --it --rm --entrypoint /usr/local/bin/cal_twin_win_bcd_cnt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cal_twin_win_bcd_cnt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cluster_reads

```bash
$ singularity exec <container> /usr/local/bin/cluster_reads
$ podman run --it --rm --entrypoint /usr/local/bin/cluster_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cnv_detection

```bash
$ singularity exec <container> /usr/local/bin/cnv_detection
$ podman run --it --rm --entrypoint /usr/local/bin/cnv_detection   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnv_detection   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_barcode_info

```bash
$ singularity exec <container> /usr/local/bin/extract_barcode_info
$ podman run --it --rm --entrypoint /usr/local/bin/extract_barcode_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_barcode_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fermi2

```bash
$ singularity exec <container> /usr/local/bin/fermi2
$ podman run --it --rm --entrypoint /usr/local/bin/fermi2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fermi2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fermi2.pl

```bash
$ singularity exec <container> /usr/local/bin/fermi2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fermi2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fermi2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grid_overlap

```bash
$ singularity exec <container> /usr/local/bin/grid_overlap
$ podman run --it --rm --entrypoint /usr/local/bin/grid_overlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grid_overlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapdip.js

```bash
$ singularity exec <container> /usr/local/bin/hapdip.js
$ podman run --it --rm --entrypoint /usr/local/bin/hapdip.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapdip.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsbox

```bash
$ singularity exec <container> /usr/local/bin/htsbox
$ podman run --it --rm --entrypoint /usr/local/bin/htsbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linkedsv.py

```bash
$ singularity exec <container> /usr/local/bin/linkedsv.py
$ podman run --it --rm --entrypoint /usr/local/bin/linkedsv.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linkedsv.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### output_bam_coreinfo

```bash
$ singularity exec <container> /usr/local/bin/output_bam_coreinfo
$ podman run --it --rm --entrypoint /usr/local/bin/output_bam_coreinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/output_bam_coreinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_sparse_nodes

```bash
$ singularity exec <container> /usr/local/bin/remove_sparse_nodes
$ podman run --it --rm --entrypoint /usr/local/bin/remove_sparse_nodes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_sparse_nodes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ropebwt2

```bash
$ singularity exec <container> /usr/local/bin/ropebwt2
$ podman run --it --rm --entrypoint /usr/local/bin/ropebwt2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ropebwt2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-calling

```bash
$ singularity exec <container> /usr/local/bin/run-calling
$ podman run --it --rm --entrypoint /usr/local/bin/run-calling   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-calling   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### small_deletion_detection

```bash
$ singularity exec <container> /usr/local/bin/small_deletion_detection
$ podman run --it --rm --entrypoint /usr/local/bin/small_deletion_detection   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/small_deletion_detection   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimadap

```bash
$ singularity exec <container> /usr/local/bin/trimadap
$ podman run --it --rm --entrypoint /usr/local/bin/trimadap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimadap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimadap-mt

```bash
$ singularity exec <container> /usr/local/bin/trimadap-mt
$ podman run --it --rm --entrypoint /usr/local/bin/trimadap-mt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimadap-mt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtk

```bash
$ singularity exec <container> /usr/local/bin/seqtk
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qconvex

```bash
$ singularity exec <container> /usr/local/bin/qconvex
$ podman run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdelaunay

```bash
$ singularity exec <container> /usr/local/bin/qdelaunay
$ podman run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhalf

```bash
$ singularity exec <container> /usr/local/bin/qhalf
$ podman run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhull

```bash
$ singularity exec <container> /usr/local/bin/qhull
$ podman run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvoronoi

```bash
$ singularity exec <container> /usr/local/bin/qvoronoi
$ podman run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbox

```bash
$ singularity exec <container> /usr/local/bin/rbox
$ podman run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam

```bash
$ singularity exec <container> /usr/local/bin/bedToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToIgv

```bash
$ singularity exec <container> /usr/local/bin/bedToIgv
$ podman run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtools

```bash
$ singularity exec <container> /usr/local/bin/bedtools
$ podman run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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