---
layout: container
name:  "quay.io/biocontainers/fusion-filter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fusion-filter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fusion-filter/container.yaml"
updated_at: "2026-01-10 03:43:50.235604"
latest: "0.5.0--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/fusion-filter"
aliases:
 - "atoiindex"
 - "blast_and_promiscuity_filter.pl"
 - "blast_check_pair.pl"
 - "blast_filter.pl"
 - "blast_outfmt6_replace_trans_id_w_gene_symbol.pl"
 - "build_chr_gene_alignment_index.pl"
 - "build_fusion_annot_db_index.pl"
 - "build_prot_info_db.pl"
 - "cmetindex"
 - "cpuid"
 - "dbsnp_iit"
 - "ensembl_genes"
 - "fa_coords"
 - "gencode_extract_relevant_gtf_exons.pl"
 - "get-genome"
 - "gff3_genes"
 - "gff3_introns"
 - "gff3_splicesites"
 - "gmap.nosimd"
 - "gmap.sse42"
 - "gmap_build"
 - "gmap_cat"
 - "gmap_process"
 - "gmapindex"
 - "gmapl"
 - "gmapl.nosimd"
 - "gmapl.sse42"
 - "gsnap"
 - "gsnap.nosimd"
 - "gsnap.sse42"
 - "gsnapl"
 - "gsnapl.nosimd"
 - "gsnapl.sse42"
 - "gtf_file_to_feature_seqs.pl"
 - "gtf_genes"
 - "gtf_introns"
 - "gtf_splicesites"
 - "gtf_to_exon_gene_records.pl"
 - "gtf_to_gene_spans.pl"
 - "gtf_transcript_splicesites"
 - "gvf_iit"
 - "iit_dump"
 - "iit_get"
 - "iit_store"
 - "index_blast_pairs.pl"
 - "index_blast_pairs.remove_gene_pair.pl"
 - "index_blast_pairs.remove_overlapping_genes.pl"
 - "index_cdna_seqs.pl"
 - "index_pfam_domain_info.pl"
 - "indexdb_cat"
 - "isoform_blast_gene_chr_conversion.pl"
 - "isoform_blast_mapping_indexer.pl"
 - "just_blast_test.pl"
 - "make_super_locus.pl"
 - "md_coords"
 - "prep_genome_lib.pl"
 - "promiscuity_filter.pl"
 - "psl_genes"
 - "psl_introns"
 - "psl_splicesites"
 - "remove_long_intron_readthru_transcripts.pl"
 - "sam_sort"
 - "snpindex"
 - "trindex"
 - "vcf_iit"
 - "gmap"
 - "STAR"
 - "STARlong"
 - "blast_report"
 - "blastdb_convert"
 - "blastdb_path"
 - "certtool"
 - "gnutls-cli"
 - "gnutls-cli-debug"
 - "gnutls-serv"
versions:
 - "0.5.0--hdfd78af_3"
 - "0.5.0--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for fusion-filter"
config: {"url": "https://biocontainers.pro/tools/fusion-filter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fusion-filter", "latest": {"0.5.0--hdfd78af_4": "sha256:ceecbb2ca1a763aab72563247282df25a5b65d5987476c29da045e2001b63808"}, "tags": {"0.5.0--hdfd78af_3": "sha256:6fc5fbea4f138208039a0a4f8383239dbfc68134ecc4570996869bff167e81f4", "0.5.0--hdfd78af_4": "sha256:ceecbb2ca1a763aab72563247282df25a5b65d5987476c29da045e2001b63808"}, "docker": "quay.io/biocontainers/fusion-filter", "aliases": {"atoiindex": "/usr/local/bin/atoiindex", "blast_and_promiscuity_filter.pl": "/usr/local/bin/blast_and_promiscuity_filter.pl", "blast_check_pair.pl": "/usr/local/bin/blast_check_pair.pl", "blast_filter.pl": "/usr/local/bin/blast_filter.pl", "blast_outfmt6_replace_trans_id_w_gene_symbol.pl": "/usr/local/bin/blast_outfmt6_replace_trans_id_w_gene_symbol.pl", "build_chr_gene_alignment_index.pl": "/usr/local/bin/build_chr_gene_alignment_index.pl", "build_fusion_annot_db_index.pl": "/usr/local/bin/build_fusion_annot_db_index.pl", "build_prot_info_db.pl": "/usr/local/bin/build_prot_info_db.pl", "cmetindex": "/usr/local/bin/cmetindex", "cpuid": "/usr/local/bin/cpuid", "dbsnp_iit": "/usr/local/bin/dbsnp_iit", "ensembl_genes": "/usr/local/bin/ensembl_genes", "fa_coords": "/usr/local/bin/fa_coords", "gencode_extract_relevant_gtf_exons.pl": "/usr/local/bin/gencode_extract_relevant_gtf_exons.pl", "get-genome": "/usr/local/bin/get-genome", "gff3_genes": "/usr/local/bin/gff3_genes", "gff3_introns": "/usr/local/bin/gff3_introns", "gff3_splicesites": "/usr/local/bin/gff3_splicesites", "gmap.nosimd": "/usr/local/bin/gmap.nosimd", "gmap.sse42": "/usr/local/bin/gmap.sse42", "gmap_build": "/usr/local/bin/gmap_build", "gmap_cat": "/usr/local/bin/gmap_cat", "gmap_process": "/usr/local/bin/gmap_process", "gmapindex": "/usr/local/bin/gmapindex", "gmapl": "/usr/local/bin/gmapl", "gmapl.nosimd": "/usr/local/bin/gmapl.nosimd", "gmapl.sse42": "/usr/local/bin/gmapl.sse42", "gsnap": "/usr/local/bin/gsnap", "gsnap.nosimd": "/usr/local/bin/gsnap.nosimd", "gsnap.sse42": "/usr/local/bin/gsnap.sse42", "gsnapl": "/usr/local/bin/gsnapl", "gsnapl.nosimd": "/usr/local/bin/gsnapl.nosimd", "gsnapl.sse42": "/usr/local/bin/gsnapl.sse42", "gtf_file_to_feature_seqs.pl": "/usr/local/bin/gtf_file_to_feature_seqs.pl", "gtf_genes": "/usr/local/bin/gtf_genes", "gtf_introns": "/usr/local/bin/gtf_introns", "gtf_splicesites": "/usr/local/bin/gtf_splicesites", "gtf_to_exon_gene_records.pl": "/usr/local/bin/gtf_to_exon_gene_records.pl", "gtf_to_gene_spans.pl": "/usr/local/bin/gtf_to_gene_spans.pl", "gtf_transcript_splicesites": "/usr/local/bin/gtf_transcript_splicesites", "gvf_iit": "/usr/local/bin/gvf_iit", "iit_dump": "/usr/local/bin/iit_dump", "iit_get": "/usr/local/bin/iit_get", "iit_store": "/usr/local/bin/iit_store", "index_blast_pairs.pl": "/usr/local/bin/index_blast_pairs.pl", "index_blast_pairs.remove_gene_pair.pl": "/usr/local/bin/index_blast_pairs.remove_gene_pair.pl", "index_blast_pairs.remove_overlapping_genes.pl": "/usr/local/bin/index_blast_pairs.remove_overlapping_genes.pl", "index_cdna_seqs.pl": "/usr/local/bin/index_cdna_seqs.pl", "index_pfam_domain_info.pl": "/usr/local/bin/index_pfam_domain_info.pl", "indexdb_cat": "/usr/local/bin/indexdb_cat", "isoform_blast_gene_chr_conversion.pl": "/usr/local/bin/isoform_blast_gene_chr_conversion.pl", "isoform_blast_mapping_indexer.pl": "/usr/local/bin/isoform_blast_mapping_indexer.pl", "just_blast_test.pl": "/usr/local/bin/just_blast_test.pl", "make_super_locus.pl": "/usr/local/bin/make_super_locus.pl", "md_coords": "/usr/local/bin/md_coords", "prep_genome_lib.pl": "/usr/local/bin/prep_genome_lib.pl", "promiscuity_filter.pl": "/usr/local/bin/promiscuity_filter.pl", "psl_genes": "/usr/local/bin/psl_genes", "psl_introns": "/usr/local/bin/psl_introns", "psl_splicesites": "/usr/local/bin/psl_splicesites", "remove_long_intron_readthru_transcripts.pl": "/usr/local/bin/remove_long_intron_readthru_transcripts.pl", "sam_sort": "/usr/local/bin/sam_sort", "snpindex": "/usr/local/bin/snpindex", "trindex": "/usr/local/bin/trindex", "vcf_iit": "/usr/local/bin/vcf_iit", "gmap": "/usr/local/bin/gmap", "STAR": "/usr/local/bin/STAR", "STARlong": "/usr/local/bin/STARlong", "blast_report": "/usr/local/bin/blast_report", "blastdb_convert": "/usr/local/bin/blastdb_convert", "blastdb_path": "/usr/local/bin/blastdb_path", "certtool": "/usr/local/bin/certtool", "gnutls-cli": "/usr/local/bin/gnutls-cli", "gnutls-cli-debug": "/usr/local/bin/gnutls-cli-debug", "gnutls-serv": "/usr/local/bin/gnutls-serv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fusion-filter.
shpc-registry automated BioContainers addition for fusion-filter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fusion-filter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fusion-filter:0.5.0--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fusion-filter/0.5.0--hdfd78af_4
$ module help quay.io/biocontainers/fusion-filter/0.5.0--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fusion-filter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fusion-filter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fusion-filter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fusion-filter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fusion-filter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fusion-filter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### atoiindex

```bash
$ singularity exec <container> /usr/local/bin/atoiindex
$ podman run --it --rm --entrypoint /usr/local/bin/atoiindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/atoiindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_and_promiscuity_filter.pl

```bash
$ singularity exec <container> /usr/local/bin/blast_and_promiscuity_filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast_and_promiscuity_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_and_promiscuity_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_check_pair.pl

```bash
$ singularity exec <container> /usr/local/bin/blast_check_pair.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast_check_pair.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_check_pair.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_filter.pl

```bash
$ singularity exec <container> /usr/local/bin/blast_filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_outfmt6_replace_trans_id_w_gene_symbol.pl

```bash
$ singularity exec <container> /usr/local/bin/blast_outfmt6_replace_trans_id_w_gene_symbol.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast_outfmt6_replace_trans_id_w_gene_symbol.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_outfmt6_replace_trans_id_w_gene_symbol.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_chr_gene_alignment_index.pl

```bash
$ singularity exec <container> /usr/local/bin/build_chr_gene_alignment_index.pl
$ podman run --it --rm --entrypoint /usr/local/bin/build_chr_gene_alignment_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_chr_gene_alignment_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_fusion_annot_db_index.pl

```bash
$ singularity exec <container> /usr/local/bin/build_fusion_annot_db_index.pl
$ podman run --it --rm --entrypoint /usr/local/bin/build_fusion_annot_db_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_fusion_annot_db_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_prot_info_db.pl

```bash
$ singularity exec <container> /usr/local/bin/build_prot_info_db.pl
$ podman run --it --rm --entrypoint /usr/local/bin/build_prot_info_db.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_prot_info_db.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmetindex

```bash
$ singularity exec <container> /usr/local/bin/cmetindex
$ podman run --it --rm --entrypoint /usr/local/bin/cmetindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmetindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpuid

```bash
$ singularity exec <container> /usr/local/bin/cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbsnp_iit

```bash
$ singularity exec <container> /usr/local/bin/dbsnp_iit
$ podman run --it --rm --entrypoint /usr/local/bin/dbsnp_iit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbsnp_iit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ensembl_genes

```bash
$ singularity exec <container> /usr/local/bin/ensembl_genes
$ podman run --it --rm --entrypoint /usr/local/bin/ensembl_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ensembl_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fa_coords

```bash
$ singularity exec <container> /usr/local/bin/fa_coords
$ podman run --it --rm --entrypoint /usr/local/bin/fa_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fa_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gencode_extract_relevant_gtf_exons.pl

```bash
$ singularity exec <container> /usr/local/bin/gencode_extract_relevant_gtf_exons.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gencode_extract_relevant_gtf_exons.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gencode_extract_relevant_gtf_exons.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get-genome

```bash
$ singularity exec <container> /usr/local/bin/get-genome
$ podman run --it --rm --entrypoint /usr/local/bin/get-genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_genes

```bash
$ singularity exec <container> /usr/local/bin/gff3_genes
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_introns

```bash
$ singularity exec <container> /usr/local/bin/gff3_introns
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_introns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_introns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_splicesites

```bash
$ singularity exec <container> /usr/local/bin/gff3_splicesites
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gmap.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gmap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap.sse42

```bash
$ singularity exec <container> /usr/local/bin/gmap.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/gmap.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_build

```bash
$ singularity exec <container> /usr/local/bin/gmap_build
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_cat

```bash
$ singularity exec <container> /usr/local/bin/gmap_cat
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_process

```bash
$ singularity exec <container> /usr/local/bin/gmap_process
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_process   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_process   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmapindex

```bash
$ singularity exec <container> /usr/local/bin/gmapindex
$ podman run --it --rm --entrypoint /usr/local/bin/gmapindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmapindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmapl

```bash
$ singularity exec <container> /usr/local/bin/gmapl
$ podman run --it --rm --entrypoint /usr/local/bin/gmapl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmapl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmapl.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gmapl.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gmapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmapl.sse42

```bash
$ singularity exec <container> /usr/local/bin/gmapl.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/gmapl.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmapl.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnap

```bash
$ singularity exec <container> /usr/local/bin/gsnap
$ podman run --it --rm --entrypoint /usr/local/bin/gsnap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnap.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gsnap.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gsnap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnap.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnap.sse42

```bash
$ singularity exec <container> /usr/local/bin/gsnap.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/gsnap.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnap.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnapl

```bash
$ singularity exec <container> /usr/local/bin/gsnapl
$ podman run --it --rm --entrypoint /usr/local/bin/gsnapl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnapl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnapl.nosimd

```bash
$ singularity exec <container> /usr/local/bin/gsnapl.nosimd
$ podman run --it --rm --entrypoint /usr/local/bin/gsnapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnapl.nosimd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnapl.sse42

```bash
$ singularity exec <container> /usr/local/bin/gsnapl.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/gsnapl.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnapl.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_file_to_feature_seqs.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf_file_to_feature_seqs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_file_to_feature_seqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_file_to_feature_seqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_genes

```bash
$ singularity exec <container> /usr/local/bin/gtf_genes
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_introns

```bash
$ singularity exec <container> /usr/local/bin/gtf_introns
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_introns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_introns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_splicesites

```bash
$ singularity exec <container> /usr/local/bin/gtf_splicesites
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_to_exon_gene_records.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf_to_exon_gene_records.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_to_exon_gene_records.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_to_exon_gene_records.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_to_gene_spans.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf_to_gene_spans.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_to_gene_spans.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_to_gene_spans.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_transcript_splicesites

```bash
$ singularity exec <container> /usr/local/bin/gtf_transcript_splicesites
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_transcript_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_transcript_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvf_iit

```bash
$ singularity exec <container> /usr/local/bin/gvf_iit
$ podman run --it --rm --entrypoint /usr/local/bin/gvf_iit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gvf_iit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iit_dump

```bash
$ singularity exec <container> /usr/local/bin/iit_dump
$ podman run --it --rm --entrypoint /usr/local/bin/iit_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iit_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iit_get

```bash
$ singularity exec <container> /usr/local/bin/iit_get
$ podman run --it --rm --entrypoint /usr/local/bin/iit_get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iit_get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iit_store

```bash
$ singularity exec <container> /usr/local/bin/iit_store
$ podman run --it --rm --entrypoint /usr/local/bin/iit_store   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iit_store   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_blast_pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/index_blast_pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_blast_pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_blast_pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_blast_pairs.remove_gene_pair.pl

```bash
$ singularity exec <container> /usr/local/bin/index_blast_pairs.remove_gene_pair.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_blast_pairs.remove_gene_pair.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_blast_pairs.remove_gene_pair.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_blast_pairs.remove_overlapping_genes.pl

```bash
$ singularity exec <container> /usr/local/bin/index_blast_pairs.remove_overlapping_genes.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_blast_pairs.remove_overlapping_genes.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_blast_pairs.remove_overlapping_genes.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_cdna_seqs.pl

```bash
$ singularity exec <container> /usr/local/bin/index_cdna_seqs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_cdna_seqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_cdna_seqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_pfam_domain_info.pl

```bash
$ singularity exec <container> /usr/local/bin/index_pfam_domain_info.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_pfam_domain_info.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_pfam_domain_info.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexdb_cat

```bash
$ singularity exec <container> /usr/local/bin/indexdb_cat
$ podman run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isoform_blast_gene_chr_conversion.pl

```bash
$ singularity exec <container> /usr/local/bin/isoform_blast_gene_chr_conversion.pl
$ podman run --it --rm --entrypoint /usr/local/bin/isoform_blast_gene_chr_conversion.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isoform_blast_gene_chr_conversion.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isoform_blast_mapping_indexer.pl

```bash
$ singularity exec <container> /usr/local/bin/isoform_blast_mapping_indexer.pl
$ podman run --it --rm --entrypoint /usr/local/bin/isoform_blast_mapping_indexer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isoform_blast_mapping_indexer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### just_blast_test.pl

```bash
$ singularity exec <container> /usr/local/bin/just_blast_test.pl
$ podman run --it --rm --entrypoint /usr/local/bin/just_blast_test.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/just_blast_test.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_super_locus.pl

```bash
$ singularity exec <container> /usr/local/bin/make_super_locus.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_super_locus.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_super_locus.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md_coords

```bash
$ singularity exec <container> /usr/local/bin/md_coords
$ podman run --it --rm --entrypoint /usr/local/bin/md_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md_coords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prep_genome_lib.pl

```bash
$ singularity exec <container> /usr/local/bin/prep_genome_lib.pl
$ podman run --it --rm --entrypoint /usr/local/bin/prep_genome_lib.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prep_genome_lib.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### promiscuity_filter.pl

```bash
$ singularity exec <container> /usr/local/bin/promiscuity_filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/promiscuity_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/promiscuity_filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl_genes

```bash
$ singularity exec <container> /usr/local/bin/psl_genes
$ podman run --it --rm --entrypoint /usr/local/bin/psl_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl_introns

```bash
$ singularity exec <container> /usr/local/bin/psl_introns
$ podman run --it --rm --entrypoint /usr/local/bin/psl_introns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl_introns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl_splicesites

```bash
$ singularity exec <container> /usr/local/bin/psl_splicesites
$ podman run --it --rm --entrypoint /usr/local/bin/psl_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl_splicesites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_long_intron_readthru_transcripts.pl

```bash
$ singularity exec <container> /usr/local/bin/remove_long_intron_readthru_transcripts.pl
$ podman run --it --rm --entrypoint /usr/local/bin/remove_long_intron_readthru_transcripts.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_long_intron_readthru_transcripts.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_sort

```bash
$ singularity exec <container> /usr/local/bin/sam_sort
$ podman run --it --rm --entrypoint /usr/local/bin/sam_sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpindex

```bash
$ singularity exec <container> /usr/local/bin/snpindex
$ podman run --it --rm --entrypoint /usr/local/bin/snpindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trindex

```bash
$ singularity exec <container> /usr/local/bin/trindex
$ podman run --it --rm --entrypoint /usr/local/bin/trindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_iit

```bash
$ singularity exec <container> /usr/local/bin/vcf_iit
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_iit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_iit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap

```bash
$ singularity exec <container> /usr/local/bin/gmap
$ podman run --it --rm --entrypoint /usr/local/bin/gmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR

```bash
$ singularity exec <container> /usr/local/bin/STAR
$ podman run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong

```bash
$ singularity exec <container> /usr/local/bin/STARlong
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_report

```bash
$ singularity exec <container> /usr/local/bin/blast_report
$ podman run --it --rm --entrypoint /usr/local/bin/blast_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_convert

```bash
$ singularity exec <container> /usr/local/bin/blastdb_convert
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_path

```bash
$ singularity exec <container> /usr/local/bin/blastdb_path
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certtool

```bash
$ singularity exec <container> /usr/local/bin/certtool
$ podman run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-cli

```bash
$ singularity exec <container> /usr/local/bin/gnutls-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-cli-debug

```bash
$ singularity exec <container> /usr/local/bin/gnutls-cli-debug
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-cli-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-cli-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnutls-serv

```bash
$ singularity exec <container> /usr/local/bin/gnutls-serv
$ podman run --it --rm --entrypoint /usr/local/bin/gnutls-serv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnutls-serv   -v ${PWD} -w ${PWD} <container> -c " $@"
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