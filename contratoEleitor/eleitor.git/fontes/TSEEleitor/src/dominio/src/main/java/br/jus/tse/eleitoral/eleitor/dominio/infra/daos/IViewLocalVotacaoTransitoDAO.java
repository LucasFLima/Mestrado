package br.jus.tse.eleitoral.eleitor.dominio.infra.daos;

import java.util.List;

import br.jus.tse.corporativa.arqjeespring.infra.daos.IBaseCRUDDAO;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.DBAcessoDadosException;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoTransito;

public interface IViewLocalVotacaoTransitoDAO extends IBaseCRUDDAO<ViewLocalVotacaoTransito, String> {

	public List<ViewLocalVotacaoTransito> findByCodObjetoEleitor(String id) throws DBAcessoDadosException;
	
}
