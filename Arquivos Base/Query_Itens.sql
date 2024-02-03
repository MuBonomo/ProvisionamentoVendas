SELECT
    marapl7.scm_matid_guid16                    AS id_material,
    marcps0.matnr                               AS material,
    maktpl7.maktx                               AS partnumber_description,
    round(((mbewps0.salk3 / mbewps0.lbkum)), 2) AS ppunit,
    marapl7.brgew                               AS peso_bruto,
    marapl7.ntgew                               AS peso_liquido,
    marapl7.gewei                               AS uom_peso,
    marapl7.volum                               AS volume,
    marapl7.voleh                               AS uom_volume,
    marapl7.laeng                               AS comprimento,
    marapl7.breit                               AS largura,
    marapl7.hoehe                               AS altura,
    marapl7.meabm                               AS uom
FROM
         mard_dali_bbm.marc_ps0 marcps0
    INNER JOIN mard_dali_ewm.mara_pl7 marapl7 ON ( marcps0.matnr = marapl7.matnr )
    INNER JOIN mard_dali_ewm.makt_pl7 maktpl7 ON ( marcps0.matnr = maktpl7.matnr )
    INNER JOIN mard_dali_bbm.mbew_ps0 mbewps0 ON ( marcps0.matnr = mbewps0.matnr )
WHERE
        marcps0.werks = 'W233'
    AND maktpl7.spras = 'E'
        AND mbewps0.bwkey = 'W233'
            AND mbewps0.lbkum != 0