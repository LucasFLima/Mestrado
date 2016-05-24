package br.jus.tse.eleitoral.eleitor.dominio.infra.daos.jpa;

import org.springframework.stereotype.Repository;

import br.jus.tse.corporativa.arqjeespring.infra.daos.jpa.AbstractBaseCRUDDAOJPA;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.DBAcessoDadosException;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.DBRecuperacaoDadosException;
import br.jus.tse.eleitoral.eleitor.dominio.infra.daos.IViewLocalVotacaoAgregacaoDAO;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoAgregacao;

@Repository
public class ViewLocalVotacaoAgregacaoDAOJPA 
	 extends AbstractBaseCRUDDAOJPA<ViewLocalVotacaoAgregacao, String> 
  implements IViewLocalVotacaoAgregacaoDAO {
	
	
	public ViewLocalVotacaoAgregacaoDAOJPA() {
		
	}
	

	@Override
	protected Class<ViewLocalVotacaoAgregacao> getEntityClass() {
		return ViewLocalVotacaoAgregacao.class;
	}

	
	@Override
	public ViewLocalVotacaoAgregacao findByCodObjetoEleitor(String id) throws DBAcessoDadosException {

		ViewLocalVotacaoAgregacao objResult = null;
		StringBuilder strHQL = null;
		
		try {

			strHQL = new StringBuilder();
			
			strHQL.append("FROM ViewLocalVotacaoAgregacao ")
				  .append("WHERE codObjetoEleitor = :codigoObjetoEleitor ");
	
			objResult = (ViewLocalVotacaoAgregacao) getEntityManager().createQuery(strHQL.toString())
																	  .setParameter("codigoObjetoEleitor", id)
																	  .getSingleResult();
		
		} catch (Exception e) {
			
			throw new DBRecuperacaoDadosException(e);
			
		}

		return objResult;
		
	}


}
