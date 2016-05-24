package br.jus.tse.eleitoral.eleitor.dominio.infra.daos;

import br.jus.tse.corporativa.arqjeespring.infra.daos.IBaseCRUDDAO;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.DBAcessoDadosException;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoAgregacao;

public interface IViewLocalVotacaoAgregacaoDAO extends IBaseCRUDDAO<ViewLocalVotacaoAgregacao, String> {

	public ViewLocalVotacaoAgregacao findByCodObjetoEleitor(String id) throws DBAcessoDadosException;
	
}
