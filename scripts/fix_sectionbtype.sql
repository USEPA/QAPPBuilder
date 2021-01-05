-- SEQUENCE: public.qar5_sectionbtypemap_id_seq

-- DROP SEQUENCE public.qar5_sectionbtypemap_id_seq;

CREATE SEQUENCE public.qar5_sectionbtypemap_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.qar5_sectionbtypemap_id_seq
    OWNER TO postgres;

---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------

-- Table: public.qar5_sectionbtypemap
-- DROP TABLE public.qar5_sectionbtypemap;
CREATE TABLE public.qar5_sectionbtypemap
(
    id integer NOT NULL DEFAULT nextval('qar5_sectionbtypemap_id_seq'::regclass),
    sectionb_type_id integer NOT NULL,
    sectiona_id integer NOT NULL,
    CONSTRAINT qar5_sectionbtypemap_pkey PRIMARY KEY (id),
    CONSTRAINT qar5_sectionbtypemap_sectiona_id_8f341e10_fk_qar5_sect FOREIGN KEY (sectiona_id)
        REFERENCES public.qar5_sectiona (qapp_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT qar5_sectionbtypemap_sectionb_type_id_fce3bd4e_fk_qar5_sect FOREIGN KEY (sectionb_type_id)
        REFERENCES public.qar5_sectionbtype (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)

TABLESPACE pg_default;

ALTER TABLE public.qar5_sectionbtypemap
    OWNER to postgres;
-- Index: qar5_sectionbtypemap_sectiona_id_8f341e10

-- DROP INDEX public.qar5_sectionbtypemap_sectiona_id_8f341e10;

CREATE INDEX qar5_sectionbtypemap_sectiona_id_8f341e10
    ON public.qar5_sectionbtypemap USING btree
    (sectiona_id ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: qar5_sectionbtypemap_sectionb_type_id_fce3bd4e

-- DROP INDEX public.qar5_sectionbtypemap_sectionb_type_id_fce3bd4e;

CREATE INDEX qar5_sectionbtypemap_sectionb_type_id_fce3bd4e
    ON public.qar5_sectionbtypemap USING btree
    (sectionb_type_id ASC NULLS LAST)
    TABLESPACE pg_default;